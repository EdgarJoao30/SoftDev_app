import streamlit as st
from PIL import Image


def app():

    st.title("Upscaling")

    st.markdown(
        """
        
        """
    )

    image = Image.open('img/endmember_decompose.png')

    st.image(image, caption='')

    
