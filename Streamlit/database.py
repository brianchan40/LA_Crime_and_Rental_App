import pandas as pd
import os

def query_db():
    
    #crime_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'processed_2010_to_Present.csv'))
    
    return pd.read_csv(os.path.join(os.path.dirname(__file__), 'condensed_crime_info.csv')).drop('Unnamed: 0', axis=1)
    
def query_zillow():
    #rental_zipcode = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Zip_zori_sm_month.csv'))
    
    return pd.read_csv(os.path.join(os.path.dirname(__file__), 'condensed_rental_data.csv')).drop('Unnamed: 0', axis=1)


    
    
if __name__ == '__main__':
    import sys
    
    print(query_zillow())