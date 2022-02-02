from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

df = pd.DataFrame(
    np.random.randn(1000, 2) / [10, 10] + [34.68, 135.49],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=34.68,
         longitude=135.49,
         zoom=10,
         pitch=45,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 500],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 0]',
             get_radius=200,
         ),
     ],
 ))