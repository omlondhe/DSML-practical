# Use the covid_vaccine_statewise.csv dataset and perform the following
# analytics.
# a. Describe the dataset
# b. Number of persons state wise vaccinated for first dose in India
# c. Number of persons state wise vaccinated for second dose in India

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('13.csv')
print(data)
print()

# describing the data
print(data.describe())
print(data.columns)
print()

# number of persons state wise vaccinated for first dose in India
aggregatedData = data.groupby(data['State']).aggregate(np.sum).reindex(columns=data.columns)
aggregatedData = aggregatedData[['First Dose Administered', 'Second Dose Administered']]
aggregatedData['First Dose Administered'] = aggregatedData['First Dose Administered'].map(int)
aggregatedData['Second Dose Administered'] = aggregatedData['Second Dose Administered'].map(int)
print(aggregatedData)
