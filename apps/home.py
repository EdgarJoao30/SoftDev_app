import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Study area")

    st.markdown(
        """
    A [streamlit](https://streamlit.io) app for: 
    Identifying and upscaling vegetation endmembers from UAV imagery to estimate 
    vegetation diversity at larger scale applications.

    The study area is located in the Peruvian Amazon, where drone data was acquired during December 2021.

    """
    )

    m = leafmap.Map(locate_control=True,
                    location = [-73.335, -3.862],
                    zoom_start=14,
                    )
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
