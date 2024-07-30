# Libraries
import streamlit as st
import streamlit.components.v1 as stc
import yaml

import pandas as pd
import numpy as np

import cv2
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.models import load_model

from ultralytics import YOLO
import PIL

import re
import unicodedata

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
            # st.write('ingredient: ', ingredient)
            # st.write('available_count: ', available_count)
            if len(available_count) == 1 and required_quantity <= available_count[0]:
                continue  # Sufficient inventory for this ingredient
            else:
                return False  # Ingredient not available in sufficient quantity
        
        return True  # All ingredients are available in sufficient quantities
    
    # Initialize variables to store found recipe name and flag
    found_recipe_name = []
    recipe_found = False
    
    # Loop through recipes
    for index, row in recipe_df.iterrows():
        if check_ingredient_availability(row, inventory_df):
            # Update inventory (simulate reservation)
            for ingredient, quantity in zip(row['main_ingredients'], row['quantity']):
                ingredient_mask = (inventory_df['ingredient_class'] == ingredient)
                if inventory_df.loc[ingredient_mask, 'ingredient_count'].values[0] >= quantity:
                    inventory_df.loc[ingredient_mask, 'ingredient_count'] -= quantity
                else:
                    break
            found_recipe_name.append(row['name'])
            recipe_found = True
            # break  # Break out of the loop once a recipe is found
    
    # If a recipe was found and updated, print confirmation
    output_df = recipe_df[recipe_df['name'].isin(found_recipe_name)]
    
    return output_df, inventory_df