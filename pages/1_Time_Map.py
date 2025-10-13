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
    lat_1 = st.number_input('lat:')
with col2:
    lon_1 = st.number_input('lon')
st.text("**Second Time Interval**")
col1, col2 = st.columns(2)
with col1:
    lat_2 = st.number_input('lat:')
with col2:
    lon_2 = st.number_input('lon')
st.text("**Third Time Interval**")
col1, col2 = st.columns(2)
with col1:
    lat_3 = st.number_input('lat:')
with col2:
    lon_3 = st.number_input('lon')
Options = ['Stremlit', 'Folium', 'Leaflet']
map_type = st.selectbox("**Select type:**",Options)

#Maps visualizations
#Comming soon!!!
