#This is the original file I am going to be working in" 

#The goal of this coding session is to clean and manipulate the 
#dataset to portray the 20th and 21th centuries meteorstrikes

#Checking if plotting mass by grams makes the graphs better?
#Saving the cleaned csv
#Create a tableau dashboard

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

#Phase 1, Data cleaning"
#Store the CSV file as data, to further work on it"
data = pd.read_csv('Meteorite_Landings.csv')

#Here we are seeing if we properly downloaded and stored the data.
data.head()

#Checking the data shape
data.shape

#Checking both if there is any null values or duplicated rows.
data.isna().sum()

data.duplicated().sum()

#Removing rows that have empty values as they will not prove to be useful for us
data = data.dropna(axis=0)

#We use info() to check the dtypes and if the amount of rows are the same.
data.info()

#Checking if the names of the columns are alright
data.columns

#Double-checking dtypes to see if its okay.
data.dtypes

#The describe function is imported to see how the numbers fluctuates
data.describe()

#In the describe() function we noticed that the maximum year is 2101, which is a year that have yet to happen.
#Therefore, we will see how many years there are after 2023.
print(data[data['year']>2023])

#As we can see its only one instance of the year being beyond 2023, we can easily get rid of it
data_sub = data[data['year']<=2023]

#Now we see that the oldest meteorite is from 2013
data_sub.describe()

#Next we simplify 'mass (g)' and make it into 'mass'.
data_sub['mass'] = data_sub['mass (g)']/1000

#And drop the 'mass (g)'.
data_sub = data_sub.drop(['mass (g)'], axis = 1)

#Lets narrow it down to the 20th and 21th century
data_20 = data_sub[data_sub['year']>1900]

#Phase 2, analysing the changed data to see patterns.
data_20.head()

#Investigating the 'fall' column as it is intriguing, where we can see that its either fallen or found
data_20['fall'].unique()

#Figuring out the mean mass of both fall and found, where we can see that the ones that were perceived falling are heavier on average.
data_20.groupby('fall')['mass'].mean()

#Here we see that there are two types, valig and relict, the latter being a meteorite inflicted by weather.
data_20['nametype'].unique()

#By grouping the nametypes by the mean mass we can see that the ones that are Relict are incredibly small on average
data_20.groupby('nametype')['mass'].mean()

#Here we can see that the heaviest Classes tend to be Iron, and the bottom two are Relict
data_20.groupby('recclass')['mass'].mean().sort_values(ascending=False)

#Checking which years have the most meteorite rainfall
data_20['year'].value_counts()

#Next we are gonna visualise the meteorite strikes on the world using geopandas
import geopandas as gpd

countries = gpd.read_file(
               gpd.datasets.get_path("naturalearth_lowres"))
countries.head()

countries.plot(color="lightgrey")

#Lets make a dataset version containing the year with the most meteorstrikes and plot it
data_79 = data_sub[data_sub['year']==1979]

#Plot for meteorstrikes after 1900s
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

#Plot for 1979 and mass
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

#Plotting a histogram with all the counted meteorstrikes from the 20th and 21th century
plt.hist(data_20['year'], bins=np.arange(data_20['year'].min(), data_20['year'].max(), 1), color = 'green', ec='black' )

#Plotting the scatter graph we can see that theres a couple of really high outliers
#After investigating, we found out that the 60 ton meteorite is the Hoba meteorite from 80000 years ago
plt.scatter(data=data_20, x='year',y='mass')

#As this meteorite was found in 1920 but fell 80000 years ago, we decided to narrow the list 
#down to only meteorites which fell in the 20th and 21th century.
data_20 = data_20[data_20['fall']=='Fell']

data_20 = data_20.drop(['fall'],axis =1)

#Majority of the meteorites that fell down in the 20/21th century were under 1 ton, except for a few outliers
plt.scatter(data=data_20, x='year',y='mass')

#Now that we are done with the dataset, lets save it and continue working on our dashboard in tableau.
data_20.to_csv('data_20.csv', index=False)
