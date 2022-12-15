# Use the covid_vaccine_statewise.csv dataset and perform the following analytics.
# A. Describe the dataset.
# B. Number of Males vaccinated
# C. Number of females vaccinated

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('13.csv')
print(data)

# describing data
print(data.describe())
print(data.columns)
print()

# number of males and females vaccinated
aggregatedData = data.groupby(data['State']).aggregate(np.sum).reindex(columns=data.columns)
aggregatedData = aggregatedData[['Male(Individuals Vaccinated)', 'Female(Individuals Vaccinated)']]
aggregatedData['Male(Individuals Vaccinated)'] = aggregatedData['Male(Individuals Vaccinated)'].map(int)
aggregatedData['Female(Individuals Vaccinated)'] = aggregatedData['Female(Individuals Vaccinated)'].map(int)
print(aggregatedData)
