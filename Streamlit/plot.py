import folium
from database import *
import pandas as pd

def plot(map_in_func, crime_df, zillow_df, crime_min, crime_max, rent_min, rent_max):
    
    final_df = pd.merge(crime_df, zillow_df, on='neighborhood')
    
    bins_safety = list(final_df["Safety_Index"].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))
    bins_zillow = list(final_df["zillow_index"].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))
    
    dict_convert = {"0":0, "0.1":1, "0.2":2, "0.3":3, "0.4":4, "0.5":5, "0.6":6, "0.7":7, "0.8":8, "0.9":9, "1":10}
    dict_convert_rent_min = {"<1800":0, "2000":2000, "2200":2200, "2400":2400, "2600":2600, "2800":2800, "3000":3000, "3200":3200, "3400":3400, "3600":3600, "3800":3800, ">4000":4000}
    dict_convert_rent_max = {"<1800":1800, "2000":2000, "2200":2200, "2400":2400, "2600":2600, "2800":2800, "3000":3000, "3200":3200, "3400":3400, "3600":3600, "3800":3800, ">4000":100000000000}
    
    for i in range(0, len(final_df.index)-1):

        if final_df.loc[i]['Safety_Index'] >= bins_safety[dict_convert[crime_min]] and final_df.loc[i]['Safety_Index'] <= bins_safety[dict_convert[crime_max]]:
            if final_df.loc[i]['zillow_index'] >= dict_convert_rent_min[rent_min] and final_df.loc[i]['zillow_index'] <= dict_convert_rent_max[rent_max]:
                
        
                folium.Marker(
                    [final_df.loc[i]['lat'], final_df.loc[i]['lon']], popup= "Zipcode: " + str(final_df.loc[i]['neighborhood']) + " Zillow Index = " + str(round(final_df.loc[i]['zillow_index'], 2))
                ).add_to(map_in_func)
    
    return map_in_func



def plot_crime_map(final_df):
    
    map_in_func = folium.Map(location=(34.045015, -118.299997))
    
    bins_safety = list(final_df["Safety_Index"].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))

    folium.Choropleth(
        geo_data="../Other_Data/LA_County_ZIP_Codes.geojson",
        name="choropleth",
        data=final_df,
        columns=["neighborhood", "Safety_Index"],
        key_on="feature.properties.ZIPCODE",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Safety Index",
        bins=bins_safety,
        reset=True,
    ).add_to(map_in_func)

    folium.LayerControl().add_to(map_in_func)
    
    return map_in_func
    
    
if __name__ == '__main__':
    final_df = query_db()
    plot_crime_map(final_df)