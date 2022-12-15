# Perform Data Cleaning, Data transformation using Python on any data set.

dataset = {
    "Age": ["10", None, "21", "22", None],
    "Name": ["Om", "Bhargavi", "Luffy", "Abhishek", "Sharva"],
    "BHK": ["1 BHK", "2", "1 BHK", "2 BHK", "3"]
}

import pandas as pd

data = pd.DataFrame(dataset)
print(data)

# finding null values
print(data.isna().sum())
# cleaning null values
data['Age'] = data['Age'].fillna(method="ffill")
print(data.isna().sum())

# transforming data
print(data['Age'].unique())
print(data['Name'].unique())
print(data['BHK'].unique())

data['BHK'] = data['BHK'].apply(lambda x: x.split()[0])

print("\nCleaned data:")
print(data)

