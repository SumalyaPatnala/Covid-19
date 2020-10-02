import pandas as pd
import geopandas as gpd
import PIL
import io

india_Covid_df = pd.read_csv('india_Covid_Dated.csv',index_col='Date')

india_Covid_df_dated=india_Covid_df.T

#reading in the Indian map shape file 
india = gpd.read_file(r'D:\COVID-19-master\csse_covid_19_data\csse_covid_19_time_series\India_States.shp')


#merging the 'india_Covid_df' and 'india' geopandas data frame
merge = india.join(india_Covid_df_dated, on='state_name', how='right')

image_frames = []

for dates in merge.columns.to_list()[9:253]:
    
    #plot
    ax = merge.plot(column = dates,
                    cmap = 'OrRd',
                    figsize = (14,14),
                    legend = True,
                    scheme = 'user_defined',
                    classification_kwds = {'bins':[10,20,50,100,500,1000,5000,10000,500000,1000000,5000000]},
                    edgecolor = 'black',
                    linewidth = 0.4)
    
    # Add a title to the map
    ax.set_title('Total Confirmed Coronavirus Cases: '+dates, fontdict = {'fontsize': 20}, pad=12.5)
    
    # Removing the axes
    ax.set_axis_off()
    
    # move the legend
    ax.get_legend().set_bbox_to_anchor((0.18,0.4))
    
    img = ax.get_figure()
    f=io.BytesIO()
    img.savefig(f, format = 'png', bbox_inches = 'tight')
    f.seek(0)
    image_frames.append(PIL.Image.open(f))
    
f.close()

#creating a gif animation
image_frames[0].save("Covid-19 Dynamics across Indian States.gif", format = 'GIF',
                     append_images = image_frames[1:],
                     save_all = True, duration = 300,
                     loop = 3)