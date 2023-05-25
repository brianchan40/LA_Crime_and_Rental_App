import streamlit as st

from database import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import numpy as np
import math



st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Where2LiveLA! 👋")

st.markdown(
    """
    Are you trying to figure out where in LA City to live? This decision is no joke, given the $$$ it costs to rent a place, and also the many areas that potentially could be more dangerous than you would like, for your family and for living comfortably. \n
    The following is just a simple plot showing the correlation between our crime index (the higher the more dangerous) and the rent prices from Zillow - and there is an unfortunate clear inverse relationship between them!
    """
)


crime_df = query_db()
zillow_df = query_zillow()
final_df = pd.merge(crime_df, zillow_df, on='neighborhood')

def func(x, a, b, c):
    return a + b * x + c * x * x


fig, ax = plt.subplots()
ax.scatter(final_df['Safety_Index'], final_df['zillow_index'])
    
popt, pcov = curve_fit(func, final_df['Safety_Index'], final_df['zillow_index'])
y_pred = func(final_df['Safety_Index'], *popt)
r2 = r2_score(final_df['zillow_index'], y_pred)

xseq = np.linspace(0, 5, num=100)
ax.plot(xseq, func(xseq, *popt), color="k", lw=2.5)

ax.set_xlabel('Crime Index')
ax.set_ylabel('Zillow Rent Price Index')

st.pyplot(fig)

    
st.markdown(
    """
    But fear not! You have found the right place to help you with making this decision! \n
    If you click on the tab "Where2LiveLA" on the left, you will find a map sectioned by zipcode. You can then choose for yourself:
    1. The min and max percentile of the crime index across all different zipcodes within LA city
        - if you currently live in LA, you can also select a zipcode and see what crime index your zipcode has right now for reference!
        - the higher the crime index, the more unsafe that area is
        - this crime index was computed from the [crime data from LAPD](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8)
    2. The min and max rent price you would like
        - Price comes from [Zillow](https://www.zillow.com/research/data/): the mean of listed rents that fall into the 40th to 60th percentile range for all homes and apartments in that zipcode
        
    Once you've found the zipcode(s) that fit your criteria, then you can use that information to go on any rental sites to find your next home! 
    
    Best of luck with your housing search!!
    """
)


