# Model Deployment
In this folder, it contains python file necessary for deploying the recipe recommendation system which used Streamlit as the web development platform.

## Overview
1. <b>app.py</b>
This contains the front-end web application which provides an interface for the users to interact with the system: to upload ingredient images and to view recommended recipes.

2. <b>recipe_preprocess.py</b>
In this python file, it includes the preprocessing of ingredients column of recipe dataset that allows for easier retrieval for modification of quantities with desired serving size.

3. <b>get_ingredient_info.py</b>
This file extracts the inventory ingredients from the ingredients column of the recipe dataset and its corresponding modified quantity to other columns dedicated for each of them.

4. <b>yolo_prediction.py</b>
It performs the detection of the ingredients and prediction which of it. It also includes retrieving predicted image files and creating an inventory through counting the predicted labels.

5. <b>get_ingredient_score.py</b>
This file performs the calculation of ingredient consumption which contribute on which recipe will be recommended in order to optimize the food inventory.

6. <b>recommendation_process.py</b>
This performs the recommendation process by filtering recipes with no ingredients to be used, checking of ingredient availability, and updating the inventory.

## Architecture

