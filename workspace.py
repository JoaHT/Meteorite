"This is the original file I am going to be working in" 

import pandas as pd 
import numpy as np 

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
data_sub['mass'] = data_sub['mass (g)']/100

"And drop the 'mass (g)'."
data_sub = data_sub.drop(['mass (g)'], axis = 1)

"Here we are fixing a weight mistake, and making it into kgs."
data_sub['mass'] = data_sub['mass']/10

data_sub.head()

"Investigating the 'fall' column as it is intriguing, where we can see that its either fallen or found"
data_sub['fall'].unique()

