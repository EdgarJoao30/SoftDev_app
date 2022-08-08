import streamlit as st
from PIL import Image




def app():

    st.title("Endmember extraction")

    st.markdown(
        """
        Spectral unmixing is based on the assumption that each pixel can be represented as a (linear) combination of 
        the "pure" material in an image, i.e. each pixel is a mixture of different "pure" signals. 
        Usually, the endmembers are collected in the field, e.g., with an ASD field spectroradiometer, 
        to determine the spectral reflectance of the pure material. However, this is costly and time-consuming, 
        so attempts are made to obtain endmembers from the image itself. Due to the fact that the study area has a 
        fairly diverse range of species, we attempt to identify endmembers from the UAV data because the resolution 
        is much better.
        """
    )
    
    image = Image.open('img/mnf_featureSpace.png')

    st.image(image, caption='Feature Space')

    st.markdown(
        """
        Instead of using the PPI, here we the Fast Iterative Puritz Index (FIPPI) is used. 
        It has several advantages over the PPI, e.g. instead of using randomly generated vectors as initial endmembers, 
        the FIPPI produces an intial set of endmembers to speed up the process and iteratively tries to find the optimal 
        set of potential endmembers.
        """
    )

    image = Image.open('img/mnf_endmember_initial.png')
    st.image(image, caption= 'Endmember selection by FIPPI')

    st.markdown(
        """
        As you can see in the graphic above, the automatic endmember selection did not work perfectly. 
        The only endmember that was selected well is the very dark pixel on the far left of the graph. 
        This is not surprising, since we are only looking at vegetation surfaces, which is very similar in spectral behavior.

        Nevertheless, we want to try to further improve the selection of endmembers. 
        To this end, a set of potential endmembers was collected in SNAP for very bright surfaces, 
        with high values in MNF 1 and medium values in MNF 2 and bright surfaces with high MNF 2 and medium MNF 1 values. 
        The endmember selection is then improved with the Graham scan, using a convex hull to find the potential endmembers.
        """
    )

    image = Image.open('img/mnf_endmember.png')
    st.image(image, caption= "Endmember selection adjusted by Graham's scan")