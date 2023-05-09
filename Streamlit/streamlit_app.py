import streamlit as st
import pandas as pd
import numpy as np
from database import *
from plot import *
from streamlit_folium import st_folium

crime_df = query_db()
zillow_df = query_zillow()
crime_map = plot_crime_map(crime_df)

def app():
    st.title('This is my app')
    
    st.markdown('This is text with **bold** and _italic_.')
    
    list_options = ["0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
    rent_options = ["<1800", "2000", "2200", "2400", "2600", "2800", "3000", "3200", "3400", "3600", "3800", ">4000"]
    
    crime_min = st.selectbox("Lower Bound on Crime (Quantile)", list_options)
    crime_max = st.selectbox("Upper Bound on Crime (Quantile)", list_options, index=5)
    rent_min = st.selectbox("Lower Bound on Rent", rent_options)
    rent_max = st.selectbox("Upper Bound on Rent", rent_options, index=5)
    
    st_data = st_folium(plot(crime_map, crime_df, zillow_df, crime_min, crime_max, rent_min, rent_max))
    
    
    
if __name__ == '__main__':
    app()