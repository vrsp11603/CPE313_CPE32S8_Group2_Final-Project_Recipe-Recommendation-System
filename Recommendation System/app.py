# Libraries

# Streamlit is used for creating interactive web apps
import streamlit as st
import streamlit.components.v1 as stc

# YAML library is used for reading classes of inventory
import yaml

# For data manipulation
import pandas as pd
import numpy as np

# Used for applying YOLO object detection models
from ultralytics import YOLO

# Used for viewing uploaded files on streamlit
import PIL

# RE library is for string matcher that is used for finding quantities
import re

# Unicodedata is used for converting unicode fraction data
import unicodedata

# Import functions

from yolo_prediction import display_images, prediction_count
from recipe_preprocess import preprocess_ingredients, scale_recipe
from get_ingredient_info import process_ingredient_info
from get_ingredient_score import calculate_percentage_consumption
from recommendation_process import find_available_recipe_and_update_inventory


# Creating inventory dataframe
inventory = pd.DataFrame(columns = ['ingredient_class', 'ingredient_count'])

# Passing object detection classes
yaml_file_path = "C:/Users/User/Downloads/Finals_IS 2.v3i.yolov9/data.yaml"
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

class_names = data['names']
inventory['ingredient_class'] = class_names
inventory['ingredient_count'] = 0

# Recipe Dataset
orig_df = pd.read_csv("C:/Users/User/Downloads/github_allrecipes.csv")
yolov9_model_path = "C:/Users/User/Downloads/wetransfer_bestyolov6-pt_2024-07-08_1357/bestYoloV9.pt"

def main():
    st.title("Recipe Recommendation System")

    # file uploading syntax
    uploaded_files = st.file_uploader(
            "Upload Multiple Images for Ingredient Detection",
            accept_multiple_files = True,
            type = ['jpg', 'jpeg', 'png']
        )
    
    # specification for how many servings
    new_servings = st.number_input('For how many people:', min_value = 1, )

    if uploaded_files is not None:
        if st.button('Recommend'):
            with st.expander("Display images"):
                # Displaying predicted images
                display_images(uploaded_files)
            
            # Applying the counted classes on the base inventory dataframe
            new_inventory = prediction_count(uploaded_files, inventory)

            # View Inventory Dataframe
            with st.expander("Inventory"):
                new_inventory = st.data_editor(
                    data = inventory.sort_values('ingredient_count', ascending = False),
                    column_config = {
                        'ingredient_class' : "ingredient_name",
                        'ingredient_count' : st.column_config.NumberColumn(
                            'ingredient_count',
                            min_value = 0
                        )
                    },
                    disabled = ['ingredient_class'],
                    hide_index = True
                )
            
            # Preprocessing orig_df such as splitting of ingredients column for easier retrieval of values
            recipe_df = preprocess_ingredients(orig_df)
            
            # Removing nutriotional columns for display
            columns_to_keep = recipe_df.columns[:recipe_df.columns.get_loc('yield') + 1].append(recipe_df.columns[recipe_df.columns.get_loc('omega_6_fatty_acid_g') + 1:])
            
            # Scaling the recipe ingredients based on user input new serving size
            recipe_df = scale_recipe(recipe_df, new_servings)
            
            # Extraction of presence of inventory classes and its quantity
            recipe_df = process_ingredient_info(recipe_df, class_names)

            # Calculating the percentage consumption of scaled ingredients of each recipe
            recipe_df = calculate_percentage_consumption(recipe_df, new_inventory)
            
            # Recipe Recommendation returning dataframe of recommended recipes and remaining inventory
            found_recipe, updated_inventory = find_available_recipe_and_update_inventory(recipe_df, new_inventory)    
            
            with st.expander(' Recommended Recipes'):
                st.dataframe(found_recipe[['name', 'category', 'url', 'ingredients', 'directions', 'main_ingredients', 'quantity', 'percentage_consumption']], hide_index = True, use_container_width=True)
            with st.expander('Remaining Inventory:'):
                st.dataframe(updated_inventory.sort_values(['ingredient_count'], ascending = False))        
        


if __name__ == '__main__':    
    main()

