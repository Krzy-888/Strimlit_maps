#comments
import streamlit as st
import pandas as pd
#import folium
#from streamlit_folium import st_folium 
import pydeck as pdk
#Title and sidebars
st.set_page_config(
    page_title="Time Maps View",
    page_icon='🗺️'
)
#Functions 


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
Options = ['Pydeck', 'Folium', 'Leaflet + streamlit', 'Leaflet only']
map_type = st.selectbox("**Select type:**",Options)
if all([lat_1, lon_1, lat_2, lon_2, lat_3, lon_3]):
    if map_type == 'Pydeck':
        #Inputs transformation
        point = {
            "path": [[lon_1, lat_1], [lon_2, lat_2], [lon_3, lat_3]],
            "time": [0, 1, 2]
        }
        df_simple = pd.DataFrame([point])
        
        #Time slider
        time_slide = st.slider("Time:", 0, 3, 0) 
        #Layer properties
        layer = pdk.Layer(
        "TripsLayer",
        data=df_simple,
        get_path="path",  
        get_color=[0, 0, 255],
        opacity=0.8,
        width_min_pixels=5,
        rounded=True,
        trail_length=1,
        get_timestamps="time",
        current_time =time_slide
        )
        view_state = pdk.ViewState(latitude=0, longitude=0, zoom=0)
        #Map properties
        st_map = pdk.Deck(
        layers=[layer],
        map_style="dark",
        initial_view_state=view_state
        )
        st.pydeck_chart(st_map) 
    if map_type == 'Folium':
        point = {
            "lon":[lon_1, lon_2, lon_3],
            "lat": [lat_1, lat_2, lat_3],
            "time": [0, 1, 2]
        }
        df_simple = pd.DataFrame(point)
        time_slide = st.slider("Time:", 0, 2, 0)
        st_map = folium.Map()
        folium.PolyLine(list(zip(df_simple["lat"], df_simple["lon"])),
                color="blue", weight=3, opacity=0.6).add_to(st_map)
        current = df_simple.iloc[time_slide]
        folium.CircleMarker(
            location=[current["lat"], current["lon"]],
            radius=8,
            color="blue",
            fill=True,
            fill_color="blue",
            popup=f"time: {current['time']}"
        ).add_to(st_map)
        st_data = st_folium(st_map)
    if map_type == 'Leaflet + streamlit':
        point = {
            "lon":[lon_1, lon_2, lon_3],
            "lat": [lat_1, lat_2, lat_3],
            "time": [0, 1, 2]
        }
        df_simple = pd.DataFrame(point)
        time_slide = st.slider("Time:", 0, 2, 0)
        current = df_simple.iloc[time_slide]
        coordinates = f"""
        L.marker([{current['lat']}, {current['lon']}]).addTo(map)"""

        st_map = """
        <div id="map" style="height: 250px;"></div>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <script>
        var map = L.map('map').setView([0,0],0);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
            """+ coordinates +"""
        </script>
        """
        st.components.v1.html(st_map, height=520)
    if map_type == 'Leaflet only':
        samples = [
            [lat_1, lon_1],
            [lon_2, lat_2],
            [lon_3, lat_3]
        ]
        samples_str = str(samples)
        st_map = """ <div>
            <button onclick="startAnimation()">Play</button>
            <button onclick="stopAnimation()">Stop</button>
            </div>
            <div id="map" style="height: 500px;"></div>

            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

            <script>
            var map = L.map('map').setView([0,0],0);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

            """+f"""var points = {samples_str};"""+"""
            var marker = L.circleMarker(points[0], {color: 'red', radius: 8}).addTo(map);

            var interval = null;
            var i = 0;

            function startAnimation() {
            if(interval) return; // jeśli już działa, nie startuj
            interval = setInterval(() => {
            i = (i + 1) % points.length;
            marker.setLatLng(points[i]);
            }, 1000);
            }

            function stopAnimation() {
            clearInterval(interval);
            interval = null;
            }
            </script>"""
        st.components.v1.html(st_map, height=600)
#Maps visualizations
#Comming soon!!!
