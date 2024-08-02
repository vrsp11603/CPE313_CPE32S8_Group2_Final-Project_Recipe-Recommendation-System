# Libraries
import pandas as pd
import numpy as np

import tensorflow as tf

import re

# # Notes
# Check the recipe with highest percentage consumption if its ingredients are okay with the inventory
# if yes:
#     put into recommended
#     update inventory
#     calculate_recipe_consumption
#     then check until None
# else:
#     go to next recipe then check

def find_available_recipe_and_update_inventory(recipe_df, inventory_df):

    recipe_df = recipe_df[recipe_df['percentage_consumption'] != 0].sort_values(['percentage_consumption'], ascending = False)
    # Function to check ingredient availability for a single recipe row
    def check_ingredient_availability(row, inventory):
        required_quantities = {}
        
        # Calculate total quantity required for each ingredient in the recipe
        for ingredient, quantity in zip(row['main_ingredients'], row['quantity']):
            if ingredient not in required_quantities:
                required_quantities[ingredient] = 0
            required_quantities[ingredient] += quantity
        
        # Check against inventory
        for ingredient, required_quantity in required_quantities.items():
            available_count = inventory[inventory['ingredient_class'] == ingredient]['ingredient_count'].values

            if len(available_count) == 1 and required_quantity <= available_count[0]:
                # Sufficient inventory for this ingredient
                continue  
            else:
                # Ingredient not available in sufficient quantity
                return False  
        
        # All ingredients are available in sufficient quantities
        return True
    
    # Initialize variables to store found recipe name and flag
    found_recipe_name = []
    recipe_found = False
    
    # Loop through recipes
    for index, row in recipe_df.iterrows():
        if check_ingredient_availability(row, inventory_df):
            # Update inventory
            for ingredient, quantity in zip(row['main_ingredients'], row['quantity']):
                ingredient_mask = (inventory_df['ingredient_class'] == ingredient)
                if inventory_df.loc[ingredient_mask, 'ingredient_count'].values[0] >= quantity:
                    inventory_df.loc[ingredient_mask, 'ingredient_count'] -= quantity
                else:
                    break
            found_recipe_name.append(row['name'])
            recipe_found = True
    

    # If a recipe was found and updated, input to the output_df
    output_df = recipe_df[recipe_df['name'].isin(found_recipe_name)]
    
    return output_df, inventory_df