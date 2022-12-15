# Perform the following operations using Python on the data set House_Price Prediction dataset. 
# Compute standard deviation, variance and percentiles using separate commands, for each feature. 
# Create a histogram for each feature in the dataset to illustrate the feature distributions.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('03.csv')
print(data)

plt.hist(x=data.std(numeric_only=True))
plt.xlabel("Standard deviation")
plt.show()

plt.hist(x=data.var(numeric_only=True))
plt.xlabel("Variance")
plt.show()

x = []
for c in data.columns:
    t = type(data[c][0])
    if t == np.float64 or t == np.int64:
        x.append(data[c].quantile(0.5))
plt.hist(x=x)
plt.xlabel("90 Percentile")
plt.show()
