import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image


def app():

    st.title("Dimensionality reduction")

    st.markdown(
    """
    We used Minimum Noise Fraction (MNF) to reduce dimensionality of our data, 
    briefly, MNF transform the bands and orders them based on their signal to noise ratio, 
    which means that th MNF output contains steadily increasing image quality, as oposed to 
    a PCA which is based on variance.

    In the image below we can see the results of the first four MNF components on our image:
    """
    )

    image = Image.open('img/mnf_components.png')

    st.image(image, caption='MNF components')
