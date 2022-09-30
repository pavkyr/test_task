"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries
import pandas as pd
import numpy as np

# TODO Import the dataset 

path = r'./data/weather_dataset.data'

df=pd.read_table(path,skiprows=1, delim_whitespace=True)

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
df=df.rename({'Yr':'year','Mo':'month','Dy':'day'},axis=1)

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
obj=list(df.select_dtypes(include=['object']).columns)

def fixdata(df):
	columns=list(df.select_dtypes(include=['object']).columns)
	df[columns]=df[columns].stack().str.replace(',','.').unstack()
	for col in columns:
		df[col] = pd.to_numeric(df[col],errors='coerce')
	df.loc9=df.loc9.clip(upper=df.loc9.quantile(0.99))
	df=df.clip(lower=0)
	return df

df=fixdata(df)

# TODO Write a function in order to fix date (this relate only to the year info) and apply it
def fixdate():
	df.year=df.year+1900

fixdate()

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
df['date']=pd.to_datetime(df[['year','month','day']])
df=df.set_index('date')

# TODO Compute how many values are missing for each location over the entire record
print(df.isna().sum())

# TODO Compute how many non-missing values there are in total
print(df.count().sum())

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
print(df[obj].mean().mean())

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
loc_stats=df[obj].describe().loc[['mean','std','max','min']]

# TODO Find the average windspeed in January for each location
print(df[df.month==1][obj].mean())

# TODO Downsample the record to a yearly frequency for each location
yearly=df.groupby((pd.PeriodIndex(df.index, freq="Y")))[obj].mean()
print(yearly)

# TODO Downsample the record to a monthly frequency for each location
monthly=df.groupby((pd.PeriodIndex(df.index, freq="M")))[obj].mean()
print(monthly)

# TODO Downsample the record to a weekly frequency for each location
weekly=df.groupby((pd.PeriodIndex(df.index, freq="W")))[obj].mean()
print(weekly)

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
print(weekly.drop(weekly.index[0]).head(21).describe().loc[['mean','min','std','max']])