import imghdr
import os
import numpy as np 
import pandas as pd
import streamlit as st
from pathlib import Path
import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap
st.set_page_config(layout="wide")



DEFAULT_DATA_BASE_DIR='./'
# model=load_model(r'assets/custom_4370_32_100_v2.h5')


# -------------------------- SIDE BAR --------------------------------
SIDEBAR_OPTION_HEATMAP = "Heatmap"
SIDEBAR_OPTION_PROJECT_INFO = "Show Project Info"
SIDEBAR_OPTION_MEET_TEAM = "Meet the Team"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_INFO,SIDEBAR_OPTION_HEATMAP,
                   SIDEBAR_OPTION_MEET_TEAM]

# st.sidebar.image("assets/facemasklogo1.png")
st.sidebar.write(" ------ ")
st.sidebar.title("Explore the Following")


# --------------------------- Functions ----------------------------------

# def read_markdown_file(markdown_file):
#     return Path(markdown_file).read_text()





# ------------------------- Selection From SideBar ------------------

app_mode = st.sidebar.selectbox(
    "Please select from the following", SIDEBAR_OPTIONS)



if app_mode == SIDEBAR_OPTION_HEATMAP:
    st.title('Heatmaps')

    # filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    filepath="./predictions.csv"
    m = leafmap.Map(tiles="stamentoner")
    # m.add_basemap("Stamen.Toner")
    m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="prediction", name="Heat map", radius=20)
    m.to_streamlit(width=700, height=500)

    



elif app_mode == SIDEBAR_OPTION_PROJECT_INFO:
    st.sidebar.success("Project information showing on the right!")
    # intro_markdown = read_markdown_file(os.path.join(DEFAULT_DATA_BASE_DIR,"README.md"))
    # st.markdown(intro_markdown, unsafe_allow_html=True)

    


    
    
    
    
    
elif app_mode == SIDEBAR_OPTION_MEET_TEAM:
    st.sidebar.write(" ------ ")
    st.markdown("<h1 style='text-align: center; color: white;'>Team MASKD!</h1>", unsafe_allow_html=True)
    st.write("------")
    st.sidebar.write('Please feel free to connect with us on Linkedin!')
    st.sidebar.success('Hope you had a great time :)')
    col1,col2,col3 = st.beta_columns([2,2,2])
    # with col1:
	#     st.image(os.path.join(DEFAULT_DATA_BASE_DIR,TEAM_DIR,'kv.jpeg'),caption="Karanveer Sidana",use_column_width=True)
    # with col2:
    #     st.image(os.path.join(DEFAULT_DATA_BASE_DIR,TEAM_DIR,'h2.jpeg'),caption="Hiten Goyal",use_column_width=True)
    # with col3:
	#     st.image(os.path.join(DEFAULT_DATA_BASE_DIR,TEAM_DIR,'channa.png'),caption="Charanjeet Singh",use_column_width=True)

    expandar_linkedin = st.beta_expander('Contact Information')
    expandar_linkedin.write(
        'Karan: https://www.linkedin.com/in/karanveer-sidana-07a49b1b1/')
    expandar_linkedin.write('Hiten: https://www.linkedin.com/in/hitengoyal/')
    expander_faq = st.beta_expander("More About Our Project")
    expander_faq.write("Hi there! If you have any questions about our project, or simply want to check out the source code, please visit our github repo: https://github.com/KingK619/Facemask-Detection")

else:
	raise ValueError(
        'Selected sidebar option is not implemented. Please open an issue on Github: ')

