import pandas as pd
import os

def query_db():
    
    crime_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'processed_2010_to_Present.csv'))
    
    return crime_data[crime_data['year'] == 2023].copy()
    
def query_zillow():
    rental_zipcode = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Zip_zori_sm_month.csv'))
    
    return rental_zipcode[["RegionName", "2023-03-31"]].rename(columns={"RegionName": "neighborhood", "2023-03-31": "zillow_index"}).copy()


    
    
if __name__ == '__main__':
    import sys
    
    print(query_zillow())