import folium

def plot():
    
    bins = list(final_df["Safety_Index"].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))

    map_ = folium.Map(location=(34.045015, -118.299997))

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
        bins=bins,
        reset=True,
    ).add_to(map_)

    folium.LayerControl().add_to(map_)

    map_
    
    
if __name__ == '__main__':
    plot()