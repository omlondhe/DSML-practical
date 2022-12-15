# Use Iris flower dataset and perform following:
# 1. Create a box plot for each feature in the dataset.
# 2. Identify and discuss distributions and identify outliers from them.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('11.csv')

# distributions
for column in data.columns:
    if column == "species":
        break
    plt.hist(x=data[column])
    plt.xlabel(column)
    plt.show()

# box plot
data.plot(kind='box')
plt.show()

# outliers are detected in the box plot

