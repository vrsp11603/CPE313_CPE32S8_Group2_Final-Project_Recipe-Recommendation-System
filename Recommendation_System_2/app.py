# Libraries
pip install ultralytics


# Streamlit is used for creating interactive web apps
import streamlit as st
import streamlit.components.v1 as stc

# Reading inventory classes

# # For data manipulation
import pandas as pd
import numpy as np

# # Used for applying YOLO object detection models
from ultralytics import YOLO

# # Used for viewing uploaded files on streamlit
import PIL

# # RE library is for string matcher that is used for finding quantities
import re

# # Unicodedata is used for converting unicode fraction data
import unicodedata

def main():
    st.title("Recipe Recommendation System")

if __name__ == '__main__':    
    main()
