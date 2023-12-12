"This is the original file I am going to be working in" 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import time
from geopy.geocoders import Photon
geolocator = Photon(user_agent="measurements")

"Phase 1, Data cleaning"
"Store the CSV file as data, to further work on it"
data = pd.read_csv('Meteorite_Landings.csv')

"Here we are seeing if we properly downloaded and stored the data."
data.head()

"Checking the data shape"
data.shape

"Checking both if there is any null values or duplicated rows."
data.isna().sum()

data.duplicated().sum()

"Removing rows that have empty values as they will not prove to be useful for us"
data = data.dropna(axis=0)

"We use info() to check the dtypes and if the amount of rows are the same."
data.info()

"Checking if the names of the columns are alright"
data.columns

"Double-checking dtypes to see if its okay."
data.dtypes

"The describe function is imported to see how the numbers fluctuates"
data.describe()

"In the describe() function we noticed that the maximum year is 2101, which is a year that have yet to happen."
"Therefore, we will see how many years there are after 2023."
print(data[data['year']>2023])

"As we can see its only one instance of the year being beyond 2023, we can easily get rid of it"
data_sub = data[data['year']<=2023]

"Now we see that the oldest meteorite is from 2013"
data_sub.describe()

"Next we simplify 'mass (g)' and make it into 'mass'."
data_sub['mass'] = data_sub['mass (g)']/1000

"And drop the 'mass (g)'."
data_sub = data_sub.drop(['mass (g)'], axis = 1)

"Phase 2, analysing the changed data to see patterns."
data_sub.head()

"Investigating the 'fall' column as it is intriguing, where we can see that its either fallen or found"
data_sub['fall'].unique()

"Figuring out the mean mass of both fall and found, where we can see that the ones that were perceived falling are heavier on average."
data_sub.groupby('fall')['mass'].mean()

"Here we see that there are two types, valig and relict, the latter being a meteorite inflicted by weather."
data_sub['nametype'].unique()

"By grouping the nametypes by the mean mass we can see that the ones that are Relict are incredibly small on average"
data_sub.groupby('nametype')['mass'].mean()

"Here we can see that the heaviest Classes tend to be Iron, and the bottom two are Relict"
data_sub.groupby('recclass')['mass'].mean().sort_values(ascending=False)

"Checking which years have the most meteorite rainfall"
data_sub['year'].value_counts()

"Next we are gonna visualise the meteorite strikes on the world using geopandas"
import geopandas as gpd

countries = gpd.read_file(
               gpd.datasets.get_path("naturalearth_lowres"))
countries.head()

countries.plot(color="lightgrey")

"Separating our data into two groups, before and after 1900, as well as 1979 which has the highest amount of meteorstrikes."
data_19 = data_sub[data_sub['year']<=1900]
data_20 = data_sub[data_sub['year']>1900]
data_79 = data_sub[data_sub['year']==1979]

"Plot for meteorstrikes after 1900s"
fig, ax = plt.subplots(figsize=(8,6))
# plot map on axis
countries = gpd.read_file(  
     gpd.datasets.get_path("naturalearth_lowres"))
countries.plot(color="lightgrey",ax=ax)
# plot points
data_20.plot(x="reclong", y="reclat", kind="scatter", 
        c="year", colormap="cool", 
        title=f"Meteorstrikes", 
        ax=ax)
# add grid
ax.grid( alpha=0.5)
plt.show()

"Plot for 1979 and mass"
fig, ax = plt.subplots(figsize=(8,6))
# plot map on axis
countries = gpd.read_file(  
     gpd.datasets.get_path("naturalearth_lowres"))
countries.plot(color="lightgrey",ax=ax)
# plot points
data_79.plot(x="reclong", y="reclat", kind="scatter", 
        c="mass", colormap="cool", 
        title=f"Meteorstrikes", 
        ax=ax)
# add grid
ax.grid( alpha=0.5)
plt.show()


#def city_state_country(row):
    #coord = f"{row['reclat']}, {row['reclong']}"
    #location = geolocator.reverse(coord, exactly_one=True)
    #address = location.raw['properties']
    #city = address.get('city', '')
    #country = address.get('country', '')
    #row['city'] = city
    #row['country'] = country
    #return row

#data_new = data_sub.apply(city_state_country, axis=1)
#print(data_new)

