#comments
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium 

#Title and sidebars
st.set_page_config(
    page_title="Maps View",
    page_icon='🗺️'
)
st.sidebar()

#Inputs
lat = st.number_input('lat:')
lon = st.number_input('lon')
Options = ['Stremlit', 'Folium', 'Leaflet']
map_type = st.selectbox("**Select type:**",Options)

#Maps visualizations
if lat and lon:
    if map_type == 'Stremlit':
        punkt = {"lat": lat, "lon": lon}
        df_simple = pd.DataFrame([punkt])
        st_map = st.map(df_simple)  
    if map_type == 'Folium':
        punkt = {"lat": lat, "lon": lon}
        df_simple = pd.DataFrame([punkt])
        st_map = folium.Map()
        folium.Marker([lat,lon]).add_to(st_map)
        st_data = st_folium(st_map)
    if map_type == 'Leaflet':
        st_map = """
        <div id="map" style="height: 500px;"></div>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <script>
        var map = L.map('map').setView([0,0],0);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
            """+f"""
        L.marker([{lat}, {lon}]).addTo(map)
        </script>
        """
        st.components.v1.html(st_map, height=520)
