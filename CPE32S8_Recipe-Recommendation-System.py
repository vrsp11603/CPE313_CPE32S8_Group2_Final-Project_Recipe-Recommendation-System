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

inventory = pd.DataFrame(columns = ['class', 'num'])

yaml_file_path = "CPE32S8_CPE313_Finals_group2_Figueroa_Peña/Dataset/Recipe-Recommendation-System-4/data.yaml"
yolo_model_path = "CPE32S8_CPE313_Finals_group2_Figueroa_Peña/YOLOv8 Models/yolov8_v4_model1_best.pt"
cnn_model_path = "CPE32S8_CPE313_Finals_group2_Figueroa_Peña/CNNModels/CNN_Finals_Model.h5"

with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

class_names = data['names']
inventory['class'] = class_names

global stop_flag

def load_data(data):
    df = pd.read_csv(data, index_col = 0).sort_values(['Name'])
    return df

def display_with_thumbnail(row):
    image_url = row['Images']
    name = row['Name']
    thumbnail = f"<img src='{image_url}' style='width: 128px; height: 128px;'>"
    st.write(f"<br><br><div style='display: flex; align-items: center;'>{thumbnail} <p style='font-size: 32px; font-weight: bold; margin-left: 32px;'>{(name)}</p></div>", unsafe_allow_html=True)

def stop_detection():
    stop_flag = True

def knapsack_with_main_ingredients(inventory, df, total_meals):
    n = len(df)
    m = len(inventory)

    main_ingredient_quantities = {}

    for index, row in df.iterrows():
        for main_ingredient, quantity_str in zip(row['MainIngredientParts'], row['MainIngredientQuantities']):
            quantities = [q.strip(" '\"") for q in quantity_str.strip("c()").split(",")]
            for ingredient, quantity in zip(main_ingredient, quantities):
                if ingredient not in main_ingredient_quantities:
                    main_ingredient_quantities[ingredient] = 0
                try:
                    quantity_float = float(quantity)
                    main_ingredient_quantities[ingredient] += quantity_float
                except ValueError:
                    pass  

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            recipe_main_ingredients = df['MainIngredientParts'][i - 1]
            recipe_main_quantities_str = df['MainIngredientQuantities'][i - 1]
            recipe_main_quantities = [q.strip(" '\"") for q in recipe_main_quantities_str.strip("c()").split(",")]

            valid_recipe = all(main_ingredient in inventory['class'].values and 
                               (not recipe_main_quantities[k] or float(recipe_main_quantities[k]) <= inventory.loc[inventory['class'] == main_ingredient, 'num'].values[0])
                               for k, main_ingredient in enumerate(recipe_main_ingredients))

            if valid_recipe:
                dp[i][j] = max(1 + dp[i - 1][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_recipes = []
    meals_planned = 0
    i, j = n, m
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_recipes.append(df.iloc[i - 1])
            j -= 1
            meals_planned += 1
            recipe_main_ingredients = df['MainIngredientParts'][i - 1]
            recipe_main_quantities_str = df['MainIngredientQuantities'][i - 1]
            recipe_main_quantities = [q.strip(" '\"") for q in recipe_main_quantities_str.strip("c()").split(",")]
            for main_ingredient, quantity in zip(recipe_main_ingredients, recipe_main_quantities):
                if quantity:
                    inventory.loc[inventory['class'] == main_ingredient, 'num'] -= float(quantity)
        if meals_planned == total_meals:
            break
        i -= 1

    return selected_recipes, inventory

def yolo_detection(image_files):

    class_counts = {}

    st.title("Object Detection using YOLOv8")
    confidence = float(st.slider(
        "Select Model Confidence", 0, 100, 35)) / 100
    st.button('Detect Objects')
    if st.button('Stop Object Detection'):
        stop_detection()
    try:
        yolo_model = YOLO(yolo_model_path)
    except Exception as ex:
        st.error(
            f"Unable to load model. Check the specified path: {yolo_model_path}")
        st.error(ex)

    col1, col2 = st.columns(2)

    for image_file in image_files:
        with col1:          
            uploaded_image = PIL.Image.open(image_file)
            st.image(uploaded_image,
                    caption = "Uploaded Image",
                    use_column_width = True
                    )
            
        boxes = []
        
        try:     
            res = yolo_model.predict(uploaded_image,
                                conf = confidence)
            # if res and res[0].boxes:
            boxes = res[0].boxes

            res_plotted = res[0].plot()[:, :, ::-1]
        except Exception as ex:
            st.error(f"Error processing image: {ex}")
            continue
    
        with col2:
            st.image(res_plotted,
                    caption='Detected Image',
                    use_column_width=True
                    )

        try:
            for box in boxes:
                class_label = int(box.cls.item())  
                class_name = class_names[class_label] if 0 <= class_label < len(class_names) else "Unknown"
        
                if class_name not in class_counts:
                    class_counts[class_name] = 1
                else:
                    class_counts[class_name] += 1
        except Exception as ex:
            st.error(f"Error counting classes: {ex}")

    # # Summarized report
    # st.write("Summarized Object Detection Report:")
    # for class_name, count in class_counts.items():
    #     st.write(f"Class {class_name} has {count} detections.")
    
    inventory['num'] = inventory['class'].map(class_counts).fillna(0).astype(int) 

    return inventory

    # for image_file in image_files:
    #     with col1:          
    #         uploaded_image = PIL.Image.open(image_file)
    #         st.image(uploaded_image,
    #                 caption = "Uploaded Image",
    #                 use_column_width = True
    #                 )

def cnn_detection(image_files):
    cnn_model = load_model(cnn_model_path)

    def preprocess_img(image):
        resized_image = cv2.resize(image, (224, 224))  
        normalized_image = resized_image / 255.0  
        processed_image = np.expand_dims(normalized_image, axis=0)  
        return processed_image

    def postprocess_predictions(predictions, class_names):
        detected_objects = []

        # Example: Extract bounding boxes and class predictions from model output
        for prediction in predictions:
            class_index = np.argmax(prediction)  # Assuming class index is the index of the highest probability
            class_name = class_names[class_index]
            bbox = [0, 0, 100, 100]  # Example bounding box format: [xmin, ymin, width, height]
            detected_objects.append({"class": class_name, "bbox": bbox})

        return detected_objects
    
    def detect_batch(image_path):
        image = cv2.imread(image_path)
        processed_images = preprocess_img(image)
        predictions = cnn_model.predict(processed_images)
        detected_objects = postprocess_predictions(predictions, class_names)

        return detected_objects

    class_counts = {}

    st.title("Object Detection using CNN")

    col1, col2 = st.columns(2)

    for image_file in image_files:
        with col1:          
            uploaded_image = PIL.Image.open(image_file)
            st.image(uploaded_image,
                    caption = "Uploaded Image",
                    use_column_width = True
                    )    
            
        boxes = []
        
        try:     
            res = detect_batch(image_file)
            # if res and res[0].boxes:
            for i, detected_object in enumerate(res):
                image = uploaded_image[i].copy()
                for obj in res:
                    bbox = obj["bbox"]
                    cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[0]+bbox[2], bbox[1]+bbox[3]), (0, 255, 0), 2)
                    cv2.putText(image, obj["class"], (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


            res_plotted = res[0].plot()[:, :, ::-1]
        except Exception as ex:
            st.error(f"Error processing image: {ex}")
            continue
    
        with col2:
            st.image(res_plotted,
                    caption='Detected Image',
                    use_column_width=True
                    )

        try:
            for box in boxes:
                class_label = int(box.cls.item())  
                class_name = class_names[class_label] if 0 <= class_label < len(class_names) else "Unknown"
        
                if class_name not in class_counts:
                    class_counts[class_name] = 1
                else:
                    class_counts[class_name] += 1
        except Exception as ex:
            st.error(f"Error counting classes: {ex}")\
        
    inventory['num'] = inventory['class'].map(class_counts).fillna(0).astype(int) 

    return inventory
    



def main():
    st.title("Recipe Recommendation App")

    menu = ["Home", "Recommend", "Recipes", "Models", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    df = load_data("CPE32S8_CPE313_Finals_group2_Figueroa_Peña/Filipino_Cuisine_Recipe.csv")

    if choice == "Home":
        st.subheader("Home")
        # st.subheader("Interactive Calendar")
        # selected_date = st.date_input("Select a date")
        # st.write("You selected:", selected_date)

    elif choice == "Recommend":
        st.subheader("Recipe Recommendation")

        uploaded_files = st.file_uploader(
            "Upload Multiple Images for Ingredient Detection",
            accept_multiple_files = True,
            type = ['jpg', 'jpeg', 'png']
        )

        recommend_model = ['YOLO', 'CNN', 'RCNN']
        selected_model = st.selectbox("Object Detection Model:", recommend_model)

        if selected_model == "YOLO":
            # uploaded_files
            yolo_detection(uploaded_files)
            st.sidebar.subheader("Current Inventory")
            st.sidebar.dataframe(inventory.sort_values(['num'], ascending=False), height=len(inventory)*20)
            selected_recipes, updated_inventory = knapsack_with_main_ingredients(inventory, df, 21)
            st.subheader('selected_recipes')
            st.write(selected_recipes)
            st.subheader('updated_inventory')
            st.write(updated_inventory)

        elif selected_model == "CNN":
            cnn_detection(uploaded_files)
            st.sidebar.subheader("Current Inventory")
            st.sidebar.dataframe(inventory.sort_values(['num'], ascending=False), height=len(inventory)*20)
        elif selected_model == "RCNN":
            st.write("RCNN")                
            # selected_recipes, updated_inventory = knapsack_with_main_ingredients(inventory, df, 21)
            # st.subheader('selected_recipes')
            # st.write(selected_recipes)
            # st.subheader('updated_inventory')
            # st.write(updated_inventory)  
    
    elif choice == "Recipes":
        st.subheader("Recipe Dataset")
        for index, row in df.iterrows():
            display_with_thumbnail(row)    
    
    elif choice == "Models":
        st.subheader("Object Detection Models")
    
    elif choice == "About":
        st.subheader("About")
        st.text("Built with Streamlit & Pandas")        

if __name__ == '__main__':
    stop_flag = False
    main()