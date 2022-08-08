import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, dim_red, endmember, upscale  # import your app modules here

st.set_page_config(page_title="PLUS Software development S22", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": dim_red.app, "title": "Dimensionality reduction", "icon": "aspect-ratio"},
    {"func": endmember.app, "title": "Endmember extraction", "icon": "check-all"},
    {"func": upscale.app, "title": "Upscaling", "icon": "cloud-upload"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://edgarjoao30-softdev-app-streamlit-app-vy1ifg.streamlitapp.com/) is part of the final project for the Software Development Lecture at [PLUS](https://plus.ac.at/)
        
        Source code of the app: <https://github.com/EdgarJoao30/SoftDev_app>

        Source code of the processing: <https://github.com/henriDierkes/SoftwareDev_Final>
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
