import streamlit as st
import pandas as pd
import numpy as np
from database import *
from plot import plot
from streamlit_folium import st_folium

def app():
    st.title('This is my app')
    
    st.markdown('This is text with **bold** and _italic_.')
    
    list_options = ["0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
    rent_options = ["<1800", "2000", "2200", "2400", "2600", "2800", "3000", "3200", "3400", "3600", "3800", ">4000"]
    
    crime_min = st.selectbox("Lower Bound on Crime (Quantile)", list_options)
    crime_max = st.selectbox("Upper Bound on Crime (Quantile)", list_options, index=5)
    rent_min = st.selectbox("Lower Bound on Rent", rent_options)
    rent_max = st.selectbox("Upper Bound on Rent", rent_options, index=5)
    
    #map_data = pd.DataFrame(
        #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        #columns=['lat', 'lon'])

    #st.map(map_data)
    
    #st.write(plot(query_db()))
    
    st_data = st_folium(plot(query_db(), query_zillow(), crime_min, crime_max, rent_min, rent_max))
    
    
    
if __name__ == '__main__':
    app()