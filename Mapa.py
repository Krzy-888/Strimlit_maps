import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium 

lat = st.number_input('lat:')
lon = st.number_input('lon')
Options = ['Stremlit', 'Folium', 'Leaflet']
GenType = st.selectbox("**Select type:**",Options)
if lat and lon:
    if GenType == 'Stremlit':
        punkt = {"lat": lat, "lon": lon}
        df_simple = pd.DataFrame([punkt])
        st.map(df_simple)  
    if GenType == 'Folium':
        punkt = {"lat": lat, "lon": lon}
        df_simple = pd.DataFrame([punkt])
        map = folium.Map()
        folium.Marker([lat,lon]).add_to(map)
        st_data = st_folium(map)