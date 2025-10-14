#comments
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium 
import pydeck as pdk
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
Options = ['Pydeck', 'Folium', 'Leaflet']
map_type = st.selectbox("**Select type:**",Options)
if all([lat_1, lon_1, lat_2, lon_2, lat_3, lon_3]):
    if map_type == 'Pydeck':
        #Inputs transformation
        punkt = {"lat": [lat_1, lat_2, lat_3],"lon": [lon_1, lon_2, lon_3], "time":[1, 2, 3]}
        df_simple = pd.DataFrame([punkt])
        
        #Layer properties
        layer = pdk.Layer(
        "TripsLayer",
        data=df_simple,
        get_path=["lon", "lat"],  
        get_color=[0, 0, 255],
        opacity=0.8,
        width_min_pixels=5,
        rounded=True,
        trail_length=600,
        get_timestamp="time",
        )
        
        #Map properties
        st_map = pdk.Deck(
        layers=[layer],
        map_style="mapbox://styles/mapbox/light-v10",
        tooltip={"text": "lon: {lon}, lat: {lat}"}
        )
        st.pydeck_chart(st_map) 

#Maps visualizations
#Comming soon!!!
