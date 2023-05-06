import pandas as pd

def query_db():
    
    crime_data = pd.read_csv("../Crime_Data/Processed_Crime_Index/processed_2020_to_Present.csv")
    
    