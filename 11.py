# Use Iris flower dataset and perform following:
# 1. List down the features and their types (e.g., numeric, nominal) available in the dataset. 
# 2. Create a histogram for each feature in the dataset to illustrate the feature distributions.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('11.csv')

for column in data.columns:
    print(f"{column}: {type(column)}")

for column in data.columns:
    plt.hist(x=data[column])
    plt.xlabel(column)
    plt.show()
