import imghdr
import os
import numpy as np 
import pandas as pd
import streamlit as st
from pathlib import Path
import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap
st.set_page_config(layout="wide")

#data collection from api and storing it into the csv
# import data_collection                  


DEFAULT_DATA_BASE_DIR='./'
TEAM_DIR ='team/'
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

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()





# ------------------------- Selection From SideBar ------------------

app_mode = st.sidebar.selectbox(
    "Please select from the following", SIDEBAR_OPTIONS)



if app_mode == SIDEBAR_OPTION_HEATMAP:
    st.title('Heatmaps')
    filepath="./predictions.csv"
    col1,col2,col3 = st.columns([4,4,4])
    with col1:
        st.write("Australia")    
        m = leafmap.Map(center=[-30.67622,142.74998],zoom=3,tiles="stamentoner")
        m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="prediction", name="Heat map", radius=20)
        m.to_streamlit(width=350, height=350)
    with col2:
        st.write("USA")
        m = leafmap.Map(center=[36.2094194,-103.7299561],zoom=2.5,tiles="stamentoner")
        m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="prediction", name="Heat map", radius=20)
        m.to_streamlit(width=350, height=350)        
    with col3:
        st.write("Brazil")
        m = leafmap.Map(center=[-7.503517,-65.260445],zoom=2.5,tiles="stamentoner")
        m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="prediction", name="Heat map", radius=20)
        m.to_streamlit(width=350, height=350)
    st.write("")
    worldmap = '<iframe src="https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=-30.67622&lon=142.749989&zoom=0" width="100%" height="475px" frameborder="0" scroll="no"></iframe>'
    st.markdown(worldmap,unsafe_allow_html=True)


    



elif app_mode == SIDEBAR_OPTION_PROJECT_INFO:
    st.sidebar.success("Project information showing on the right!")
    intro_markdown = read_markdown_file(os.path.join(DEFAULT_DATA_BASE_DIR,"README.md"))
    st.markdown(intro_markdown, unsafe_allow_html=True)



    


    
    
    
    
    
elif app_mode == SIDEBAR_OPTION_MEET_TEAM:
    st.sidebar.write(" ------ ")
    st.markdown("<h1 style='text-align: center; color: white;'>Meet the Team</h1>", unsafe_allow_html=True)
    st.write("------")
    st.sidebar.write('Please feel free to connect with us on Linkedin!')
    st.sidebar.success('Hope you had a great time :)')
    col1,col2,col3 = st.columns([2,2,2])
    with col1:
	    st.image(os.path.join(DEFAULT_DATA_BASE_DIR,TEAM_DIR,'kv.jpeg'),caption="Karanveer Sidana",use_column_width=True)
    with col2:
        st.image(os.path.join(DEFAULT_DATA_BASE_DIR,TEAM_DIR,'hiten.jpeg'),caption="Hiten Goyal",use_column_width=True)
    with col3:
	    st.image(os.path.join(DEFAULT_DATA_BASE_DIR,TEAM_DIR,'jatin.png '),caption="Jatin Kansal",use_column_width=True)
        
    expandar_linkedin = st.expander('Contact Information')
    expandar_linkedin.write(
        'Karan: https://www.linkedin.com/in/karanveer-sidana-07a49b1b1/')
    expandar_linkedin.write('Hiten: https://www.linkedin.com/in/hitengoyal/')
    expander_faq = st.expander("More About Our Project")
    expander_faq.write("Hi there! If you have any questions about our project, or simply want to check out the source code, please visit our github repo: https://github.com/KingK619/Facemask-Detection")

else:
	raise ValueError(
        'Selected sidebar option is not implemented. Please open an issue on Github: ')

