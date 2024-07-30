import streamlit as st
import pandas as pd
import numpy as np
import re
import unicodedata

def calculate_percentage_consumption(recipe_df, inventory_df):
    def calculate_percentage(index, recipe):
        names = recipe['name']
        ingredients = recipe['main_ingredients']
        quantities = recipe['quantity']
        # st.write('index : {} \t\t\t name: {}'.format(index, names))

        
        
        total_percentage = 0
        num_ingredients = len(ingredients)

        for i in range(num_ingredients):
            ingredient = ingredients[i]
            quantity = quantities[i]


            if ingredient in inventory_df['ingredient_class'].values:
                inv_quantity = inventory_df.loc[inventory_df['ingredient_class'] == ingredient, 'ingredient_count'].values[0]
                if inv_quantity is not None:
                    if inv_quantity > 0 and quantity <= float(inv_quantity):
                        percentage = (quantity / inv_quantity) * 100
                        total_percentage += percentage
                else:
                    pass
            else:
                pass

        if num_ingredients > 0:
            average_percentage = total_percentage / inventory_df.shape[0]
        else:
            average_percentage = 0

        return round(average_percentage, 2)

    # Iterate through recipe_df using index and row (recipe)
    for index, recipe in recipe_df.iterrows():
        recipe_df.at[index, 'percentage_consumption'] = calculate_percentage(index, recipe)

    return recipe_df