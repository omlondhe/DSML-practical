# Use House_Price prediction dataset. 
# Provide summary statistics (mean, median, minimum, maximum, standard deviation) of variables 
# (categorical vs quantitative) such as 
# For example, if categorical variable is age groups and quantitative variable is income, 
# then provide summary statistics of income grouped by the age groups.

import numpy as np
import pandas as pd

data = pd.read_csv('18.csv')
print(data.columns)

print(data.mean(numeric_only=True))
print(data.median(numeric_only=True))
print(data.min(numeric_only=True))
print(data.max(numeric_only=True))
print(data.std(numeric_only=True))

groupByDate = data.groupby(data['date']).aggregate(np.sum).reindex(columns=data.columns)
print(groupByDate)
groupByStreet = data.groupby(data['street']).aggregate(np.sum).reindex(columns=data.columns)
print(groupByStreet)
groupByCity = data.groupby(data['city']).aggregate(np.sum).reindex(columns=data.columns)
print(groupByCity)
groupByStateZip = data.groupby(data['statezip']).aggregate(np.sum).reindex(columns=data.columns)
print(groupByStateZip)
groupByCountry = data.groupby(data['country']).aggregate(np.sum).reindex(columns=data.columns)
print(groupByCountry)
