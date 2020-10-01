import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#reading in the csv file
data_india = pd.read_csv('Covid-19_Across_India.csv')

#converting the available data into time-series
india_Covid_df= data_india.pivot_table('Confirmed', index='Date',
                                                        columns='State/UnionTerritory',fill_value=0)

india_Covid_df=india_Covid_df.T

#reading in the Indian map shape file 
india = gpd.read_file(r'D:\COVID-19-master\csse_covid_19_data\csse_covid_19_time_series\India_States.shp')

#checking state name discrepancies
for index, row in india_Covid_df.iterrows():
    if index not in india['state_name'].to_list():
        print(index + " is not in the shape file")
        
    else:
        pass