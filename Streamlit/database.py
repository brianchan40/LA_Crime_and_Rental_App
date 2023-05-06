import pandas as pd

def query_db():
    
    crime_data = pd.read_csv("../Crime_Data/Processed_Crime_Index/processed_2010_to_Present.csv")
    
    return crime_data[crime_data['year'] == 2023].copy()
    
    
    
if __name__ == '__main__':
    import sys
    
    print(query_db())