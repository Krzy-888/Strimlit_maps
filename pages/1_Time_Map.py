#comments
import streamlit as st
#import pandas as pd
#import folium
#from streamlit_folium import st_folium 

#Title and sidebars
st.set_page_config(
    page_title="Time Maps View",
    page_icon='🗺️'
)

#Inputs
st.text("**First Time Interval**")
col1, col2 = st.columns(2)
with col1:
    lat_1 = st.number_input('lat 1:')
with col2:
    lon_1 = st.number_input('lon 1:')
st.text("**Second Time Interval**")
col3, col4 = st.columns(2)
with col3:
    lat_2 = st.number_input('lat 2:')
with col4:
    lon_2 = st.number_input('lon 2:')
st.text("**Third Time Interval**")
col5, col6 = st.columns(2)
with col5:
    lat_3 = st.number_input('lat 3:')
with col6:
    lon_3 = st.number_input('lon 3:')
Options = ['Stremlit', 'Folium', 'Leaflet']
map_type = st.selectbox("**Select type:**",Options)

#Maps visualizations
#Comming soon!!!
