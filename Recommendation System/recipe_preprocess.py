import pandas as pd
import numpy as np
import re
import unicodedata

def preprocess_ingredients(recipe_df):
    recipe_df['ingredients'] = recipe_df['ingredients'].str.split(';')
    recipe_df['ingredients'] = recipe_df['ingredients'].apply(lambda x: [ingredient.strip() for ingredient in x])

    recipe_df = remove_parentheses(recipe_df)

    return recipe_df

def clear_text(text):
    return re.sub(r'\([^)]*\)', '', text)

def remove_parentheses(recipe_df, column_name = 'ingredients'):
    recipe_df[column_name] = recipe_df[column_name].apply(lambda arr: [clear_text(item) for item in arr])
    return recipe_df

def format_ingredients(recipe_df):
    def get_combined_quantity(ingredient):
        # Match for simple integers
        found_integer = re.search(r'\b\d+\b', ingredient)
        if found_integer:
            quantity_integer = int(found_integer.group())
        else:
            quantity_integer = None
        
        # Match for fractions and mixed numbers using unicodedata
        def replace_fraction(match):
            frac = match.group()
            if '/' in frac:
                numerator, denominator = frac.split('/')
                quantity_fraction = int(numerator) / int(denominator)
                return quantity_fraction
            else:
                numeric_value = unicodedata.numeric(frac)
                return numeric_value
        
        # Find all fractions and mixed numbers
        fractions = re.findall(r'\b(?:[\d]+[\u2044][\d]+|[\u00BC-\u00BE]|[\u2150-\u215E])\b', ingredient)
        if fractions:
            quantity_fraction = sum(replace_fraction(re.search(r'\b(?:[\d]+[\u2044][\d]+|[\u00BC-\u00BE]|[\u2150-\u215E])\b', frac)) for frac in fractions)
        else:
            quantity_fraction = None
        
        # Combine integer and fraction if both are found
        if quantity_integer is not None and quantity_fraction is not None:
            combined_quantity = quantity_integer + quantity_fraction
            ingredient = re.sub(r'\b\d+\b', '', ingredient)  # Remove standalone integers
            ingredient = re.sub(r'\b(?:[\d]+[\u2044][\d]+|[\u00BC-\u00BE]|[\u2150-\u215E])\b', str(round(combined_quantity, 2)), ingredient)
        elif quantity_fraction is not None:
            ingredient = re.sub(r'\b(?:[\d]+[\u2044][\d]+|[\u00BC-\u00BE]|[\u2150-\u215E])\b', str(round(quantity_fraction, 2)), ingredient)
        
        return ingredient.strip()
    
    recipe_df['ingredients'] = recipe_df['ingredients'].apply(lambda ingredients: [get_combined_quantity(ingredient) for ingredient in ingredients])
    
    return recipe_df

def scale_recipe(recipe_df, new_serving_size):

    recipe_df = format_ingredients(recipe_df)

    for index, recipe in recipe_df.iterrows():
        current_serving_size = recipe['servings']
        if current_serving_size != new_serving_size:
            ratio = new_serving_size / current_serving_size
            ingredients = recipe['ingredients']
            resized_ingredients = []
            for ingredient in ingredients:
                parts = ingredient.split()
                if len(parts) > 1 and parts[0].replace('.', '', 1).isdigit():
                    try:
                        value = float(parts[0])
                        new_value = value * ratio
                        # Format the new value to match the original ingredient format
                        formatted_value = "{:.2f}".format(new_value).rstrip('0').rstrip('.')
                        resized_ingredient = f"{formatted_value} {' '.join(parts[1:])}"
                        resized_ingredients.append(resized_ingredient)
                    except ValueError:
                        resized_ingredients.append(ingredient)  # Handle non-numeric parts gracefully
                else:
                    resized_ingredients.append(ingredient)

            recipe_df.at[index, 'ingredients'] = resized_ingredients

    recipe_df['servings'] = new_serving_size

    return recipe_df



def update_ingredients_mema(recipe_df, new_serving_size):
    original_serving_sizes = recipe_df['servings']
    recipe_df['servings'] = [new_serving_size] * len(recipe_df)  # Update the servings
    
    def get_combined_quantity(ingredient):
        # Helper function to extract and scale quantities
        def extract_quantity(text):
            # Match for simple integers
            found_integer = re.search(r'\b\d+\b', text)
            if found_integer:
                quantity_integer = int(found_integer.group())
            else:
                quantity_integer = 0
            
            # Match for fractions and mixed numbers using unicodedata
            def replace_fraction(match):
                frac = match.group()
                if '/' in frac:
                    numerator, denominator = frac.split('/')
                    quantity_fraction = int(numerator) / int(denominator)
                    return quantity_fraction
                else:
                    numeric_value = unicodedata.numeric(frac)
                    return numeric_value
            
            # Find all fractions and mixed numbers
            fractions = re.findall(r'\b(?:[\d]+[\u2044][\d]+|[\u00BC-\u00BE]|[\u2150-\u215E])\b', text)
            quantity_fraction = sum(replace_fraction(re.search(r'\b(?:[\d]+[\u2044][\d]+|[\u00BC-\u00BE]|[\u2150-\u215E])\b', frac)) for frac in fractions)
            
            # Combine integer and fraction
            total_quantity = quantity_integer + quantity_fraction
            return total_quantity
        
        # Extract quantity from ingredient
        quantity = extract_quantity(ingredient)
        
        # Scale quantity based on serving size
        scaling_factor = new_serving_size / original_serving_sizes
        scaled_quantity = quantity * scaling_factor
        
        # Replace the quantity in the ingredient string
        result = re.sub(r'\b\d+\b', str(round(scaled_quantity, 2)), ingredient)
        
        return result.strip()
    
    # Apply the scaling function to each recipe's ingredients list
    recipe_df['ingredients'] = recipe_df['ingredients'].apply(lambda ingredients: [get_combined_quantity(ingredient) for ingredient in ingredients])
    
    return recipe_df
