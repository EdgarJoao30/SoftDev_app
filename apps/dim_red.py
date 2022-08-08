import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image


def app():

    st.title("Dimensionality reduction")

    image = Image.open('img/mnf_components.png')

    st.image(image, caption='MNF components')
