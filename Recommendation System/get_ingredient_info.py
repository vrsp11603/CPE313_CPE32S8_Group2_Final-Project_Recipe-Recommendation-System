import pandas as pd
import numpy as np
import re
import unicodedata

def process_ingredient_info(recipe_df, ingredient_class):
    # List of things to be avoid such as tomato 'paste', chicken 'broth', 
    exclude = ['sauce', 'paste', 'powder', 'broth', 'stock', 'juice', 'wrapper', 'quail', 'root', 'sweet potato'] #, 'pounds', 'ounces']

    # This function is used to extract float values of ingredients through re and 
    # utilizing pattern that searches digits (\d*), dot (\.), and digit again (\d+)
    # considering a space after and few cooking measurements.
    def extract_quantities(ingredient, pattern = r'(\d*\.?\d+)\s*(?:cup|tablespoon|teaspoon|pound|can)?'):
        matches = re.findall(pattern, ingredient)
        if matches:
            for match in matches:
                if '.' in match:
                    return float(match)
                else:
                    return int(match)
        else:
            return 0
    
    # Creation of 2 columns for main_ingredients and corresoponding quantities
    # extraction of inventory classes and quantities
    def process_ingredients(recipe_df, ingredient_class, exclude):
        main_ingredients_data = []
        quantities_data = []
        
        for index, row in recipe_df.iterrows():
            ingredients = row['ingredients']
            ingredient_list = []
            quantity_list = []
            
            for ingredient in ingredients:
                lower_ingredient = ingredient.lower()
                contains_ingredient = any(word.lower() in lower_ingredient for word in ingredient_class)
                exclude_ingredient = any(word in lower_ingredient for word in exclude)
                
                if contains_ingredient and not exclude_ingredient:
                    main_ingredient = None
                    for main_ingredient_candidate in ingredient_class:
                        if main_ingredient_candidate.lower() in lower_ingredient:
                            main_ingredient = main_ingredient_candidate
                            break
                    
                    if main_ingredient:
                        quantity = extract_quantities(ingredient)
                        ingredient_list.append(main_ingredient)
                        quantity_list.append(quantity)
            
            main_ingredients_data.append(ingredient_list)
            quantities_data.append(quantity_list)
        
        return main_ingredients_data, quantities_data
    
    main_ingredients_data, quantities_data = process_ingredients(recipe_df, ingredient_class, exclude)
    
    recipe_df['main_ingredients'] = main_ingredients_data
    recipe_df['quantity'] = quantities_data

    recipe_df = recipe_df[recipe_df['main_ingredients'].apply(lambda x: len(x) > 0)]
    recipe_df = recipe_df[recipe_df['quantity'].apply(lambda x: len(x) > 0)]
    
    return recipe_df