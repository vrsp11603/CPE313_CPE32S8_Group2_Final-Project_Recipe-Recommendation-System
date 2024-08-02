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

import os

# Import functions
from yolo_prediction import load_image, display_images, image_prediction, prediction_count

from recipe_preprocess import preprocess_ingredients, scale_recipe

from get_ingredient_info import process_ingredient_info

from get_ingredient_score import calculate_percentage_consumption

from recommendation_process import find_available_recipe_and_update_inventory


# ...
inventory = pd.DataFrame(columns = ['ingredient_class', 'ingredient_count'])

yaml_file_path = "C:/Users/User/Downloads/Finals_IS 2.v3i.yolov9/data.yaml"
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

class_names = data['names']
inventory['ingredient_class'] = class_names
inventory['ingredient_count'] = 0

orig_df = pd.read_csv("C:/Users/User/Downloads/github_allrecipes.csv")
yolov9_model_path = "C:/Users/User/Downloads/wetransfer_bestyolov6-pt_2024-07-08_1357/bestYoloV9.pt"

def main():
    st.title("Recom System")
    st.write('Directory: ', os.getcwd())

    uploaded_files = st.file_uploader(
            "Upload Multiple Images for Ingredient Detection",
            accept_multiple_files = True,
            type = ['jpg', 'jpeg', 'png']
        )
    
    new_servings = st.number_input('For how many people:', min_value = 1, )

    if uploaded_files is not None:
        if st.button('Recommend'):
            with st.expander("Display images"):
                display_images(uploaded_files)
            
            new_inventory = prediction_count(uploaded_files, inventory)

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
            
            recipe_df = preprocess_ingredients(orig_df)
    
            columns_to_keep = recipe_df.columns[:recipe_df.columns.get_loc('yield') + 1].append(recipe_df.columns[recipe_df.columns.get_loc('omega_6_fatty_acid_g') + 1:])
            selected_columns = st.multiselect('Select columns to display', columns_to_keep)

            with st.expander('Recipe Dataset'):
                if selected_columns:
                    if 'percentage_consumption' in selected_columns:
                        st.dataframe(recipe_df[selected_columns].sort_values(['percentage_consumption'], ascending = False), hide_index = True, use_container_width=True)
                    else:
                        st.dataframe(recipe_df[selected_columns], hide_index = True, use_container_width=True)        
                else:
                    st.dataframe(recipe_df[['name', 'category', 'ingredients', 'directions', 'servings']], hide_index = True, use_container_width=True)

            recipe_df = scale_recipe(recipe_df, new_servings)
            with st.expander('Scaled Recipe Dataset'):
                st.dataframe(recipe_df[['name', 'category', 'ingredients', 'directions', 'servings']], hide_index = True, use_container_width=True)


            recipe_df = process_ingredient_info(recipe_df, class_names)
            with st.expander('process_ingredient_info Dataset'):
                st.dataframe(recipe_df[['name', 'category', 'ingredients', 'main_ingredients', 'quantity']], hide_index = True, use_container_width=True)

            # st.write(recipe_df.info())

            recipe_df = calculate_percentage_consumption(recipe_df, new_inventory)
            with st.expander('calculate_percentage_consumption Dataset'):
                st.dataframe(recipe_df[['name', 'main_ingredients', 'quantity', 'percentage_consumption']], hide_index = True, use_container_width=True)
            
            
            found_recipe, updated_inventory = find_available_recipe_and_update_inventory(recipe_df, new_inventory)    
            
            with st.expander('Found Recipes'):
                st.dataframe(found_recipe[['name', 'category', 'url', 'ingredients', 'main_ingredients', 'quantity']], hide_index = True, use_container_width=True)
                if st.button('View Full Recipe'):
                    st.dataframe(found_recipe[columns_to_keep], hide_index = True, use_container_width=True)
            with st.expander('Updated Inventory:'):
                st.dataframe(updated_inventory.sort_values(['ingredient_count'], ascending = False))        
        


if __name__ == '__main__':    
    main()

