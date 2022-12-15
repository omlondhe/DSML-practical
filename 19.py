# Write a Python program to display some basic statistical details like
# percentile, mean, standard deviation etc (Use python and pandas commands) 
# the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’ of iris.csv dataset.

import pandas as pd

data = pd.read_csv('11.csv')
print(data)

print(f"Mean: \n{data.mean(numeric_only=True)}\n")
print(f"Standard deviation: \n{data.std(numeric_only=True)}\n")
print(f"Variance: \n{data.var(numeric_only=True)}\n")
print(f"Quantile: \n{data.quantile(numeric_only=True)}\n")
print(f"Max: \n{data.max(numeric_only=True)}\n")
print(f"Min: \n{data.min(numeric_only=True)}\n")
print(f"Median: \n{data.median(numeric_only=True)}\n")
