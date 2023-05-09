import streamlit as st
import pandas as pd
import numpy as np
from database import *
from plot import *
from streamlit_folium import st_folium

crime_df = query_db()
zillow_df = query_zillow()
crime_map = plot_crime_map(crime_df)
bins_safety = list(crime_df["Safety_Index"].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))

def app():
    st.title('Where2LiveLA')
    
    st.markdown(
        """
        Here are the options that you have:\n
        Choose your current zipcode to find out what the crime index of your current location is.\n\n
        Choose the min and max percentile of crime that you would like to set for your next home.\n
        Choose the min and max Zillow Rental Index that you would like to find your next home.\n\n        
        Then you'll find all the different areas that satisfy those requirements, and you can hover over the bubbles to get further details on them!
        """
    )
    
    list_options = ["0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
    rent_options = ["<1800", "2000", "2200", "2400", "2600", "2800", "3000", "3200", "3400", "3600", "3800", ">4000"]
    
    curr_zip = st.selectbox("Your Current Zipcode", list(crime_df['neighborhood']))
    
    min_percent = 0
    max_percent = 1
    
    for index, val in enumerate(bins_safety):
        if crime_df.loc[crime_df['neighborhood'] == curr_zip, 'Safety_Index'].values[0] <= val:
            min_percent = (index-1)/10
            max_percent = index/10
            break
    
    st.write("The percentile of your current zipcode falls within (", min_percent, ", ", max_percent, ")")
    
    crime_min = st.selectbox("Lower Bound on Crime (Quantile)", list_options)
    crime_max = st.selectbox("Upper Bound on Crime (Quantile)", list_options, index=5)
    rent_min = st.selectbox("Lower Bound on Rent", rent_options)
    rent_max = st.selectbox("Upper Bound on Rent", rent_options, index=5)
    
    st_data = st_folium(plot(crime_map, crime_df, zillow_df, crime_min, crime_max, rent_min, rent_max))
    
    
    
if __name__ == '__main__':
    app()