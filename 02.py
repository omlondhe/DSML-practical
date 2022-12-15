# Perform the following operations using Python on the Telecom_Churn dataset. 
# Compute and display summary statistics for each feature available
# in the dataset using separate commands for each statistic. 
# (e.g. minimum value, maximum value, mean, range, standard deviation, variance and percentiles).

import pandas as pd
import numpy as np

data = pd.read_csv('02.csv')
print(data)
print()

# computing and printing minimum value
print("Minimum values: ")
print(data.min(numeric_only=True))
print()

# computing and printing maximum value
print("Maximum values: ")
print(data.max(numeric_only=True))
print()

# computing and printing mean value
print("Mean values: ")
print(data.mean(numeric_only=True))
print()

# computing and printing range
print("Range: ")
for column in data.columns:
    value = data[column][0]
    if type(value) == np.int64 or type(value) == np.float64:
        print(f"{column}:\t{data[column].max() - data[column].min()}")
print()

# computing and printing Standard deviation value
print("Standard deviation: ")
print(data.std(numeric_only=True))
print()

# computing and printing Variance
print("Variance: ")
print(data.var(numeric_only=True))
print()

# computing and printing Percentiles
print("Percentiles: ")
for column in data.columns:
    value = data[column][0]
    if type(value) == np.int64 or type(value) == np.float64:
        print(f"{column}:\t{data[column].quantile()}")
print()
