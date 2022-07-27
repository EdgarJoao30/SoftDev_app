import streamlit as st
import leafmap.foliumap as leafmap
import os


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

    out_dir = os.path.expanduser('~/Documents/GitHub/SoftDev_app/')
    droneimg = os.path.join(out_dir, 'test.tif')

    m = leafmap.Map(locate_control=True,
                    location = [-3.862, -73.335],
                    zoom_start=14,
                    )
    m.add_basemap("ROADMAP")
    m.add_raster(droneimg, bands=[4, 3, 2], layer_name='Drone image')
    m.to_streamlit(height=700)
