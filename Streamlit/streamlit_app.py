import streamlit as st
import pandas as pd
import numpy as np
from database import *
from plot import plot
from streamlit_folium import st_folium

def app():
    st.title('This is my app')
    
    st.markdown('This is text with **bold** and _italic_.')
    
    #map_data = pd.DataFrame(
        #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        #columns=['lat', 'lon'])

    #st.map(map_data)
    
    #st.write(plot(query_db()))
    
    st_data = st_folium(plot(query_db(), query_zillow(), "0", "0.5", "2200", "2800"))
    
    
    
if __name__ == '__main__':
    app()