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

yolov9_model_path = "C:/Users/User/Downloads/wetransfer_bestyolov6-pt_2024-07-08_1357/bestYoloV9.pt"
yaml_file_path = "C:/Users/User/Downloads/Finals_IS 2.v3i.yolov9/data.yaml"
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

class_names = data['names']

def load_image(image_files):
    uploaded_images = []
    names = []

    for img in image_files:
        filename = img.name
        names.append(filename)

    for i in range(len(image_files)):
        try:
            uploaded_image = PIL.Image.open(image_files[i])
            uploaded_images.append(uploaded_image)
        except Exception as ex:
            st.error(f"Error processing image: {ex}")

    return uploaded_images, names

def display_images(image_files, yolo_model = yolov9_model_path):
    model = YOLO(yolo_model)
    
    uploaded_images, names = load_image(image_files)
    columns = st.columns(4)
    
    for i in range(len(uploaded_images)):
        with columns[i % 4]:
            try:
                predict_image = model.predict(uploaded_images[i], conf = 0.2)
                plot_predictions = predict_image[0].plot()[:, :, ::-1]

                st.image(plot_predictions,
                         use_column_width=True)
            except Exception as ex:
                st.error(f"Error processing image: {ex}")
                continue

def image_prediction(image_files, yolo_model = yolov9_model_path):
    model = YOLO(yolo_model)

    uploaded_images, names = load_image(image_files)

    predictions = []

    for i in range(len(image_files)):
        try:
            predict_image = model.predict(uploaded_images[i], conf = 0.2)
            class_dict = predict_image[0].names
            cls_list = predict_image[0].boxes.cls.tolist()
            class_names = [class_dict[int(idx)] for idx in cls_list]
        except Exception as ex:
            st.error(f"Error processing image: {ex}")
            continue

        predictions.append(class_names)

    return predictions

def prediction_count(image_files, inventory_df):
    class_counts = {}

    predictions = image_prediction(image_files)

    # Count occurrences of each class name across all predictions
    for prediction in predictions:
        for class_name in prediction:
            if class_name in class_counts:
                if class_name == 'Chicken' or class_name == 'Garlic':
                    class_counts[class_name] += 8
                else:
                    class_counts[class_name] += 1
            else:
                if class_name == 'Chicken' or class_name == 'Garlic':
                    class_counts[class_name] = 8
                else: 
                    class_counts[class_name] = 1

    for class_name, count in class_counts.items():
        if class_name in inventory_df['ingredient_class'].values:
            idx = inventory_df.index[inventory_df['ingredient_class'] == class_name][0]
            inventory_df.at[idx, 'ingredient_count'] = count

    return inventory_df





