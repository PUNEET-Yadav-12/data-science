import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np

def enhance_image(image):
    # Enhance brightness and contrast
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)  # Increase brightness by 20%
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)  # Increase contrast by 20%
    return image

st.title("AI-Powered Image Enhancement")

# User uploads image
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png"])
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Original Image")

    # Enhance image
    enhanced_image = enhance_image(image)
    st.image(enhanced_image, caption="Enhanced Image")
