import streamlit as st
from PIL import Image


def app():

    st.title("Upscaling")

    st.markdown(
        """
        A Sentinel-2 Level 2A image for 03.08.2020 was acquired from the Open Access Hub with a cloud coverage 
        less than 5%. The image was then preprocessed in SNAP. Preprocessing included cloud masking with the Sen2Cor 
        algorithm, subsetting the bands to RGB, NIR, Red Edge 1-3, and SWIR 1 & 2 bands, and resampling of all bands to 10 m.
        """
    )

    image = Image.open('img/endmember_decompose.png')

    st.image(image, caption='')

    
