# Perform the following operations using Python on a suitable data set,
# counting unique values of data, format of each column, converting variable
# data type (e.g. from long to short, vice versa), identifying missing values
# and filling in the missing values.

dataset = {
    "Age": ["10", None, "21", "22", None],
    "Name": ["Om", "Bhargavi", "Luffy", "Abhishek", "Sharva"],
    "BHK": ["1 BHK", "2", "1 BHK", "2 BHK", "3"]
}

import pandas as pd

data = pd.DataFrame(dataset)
print(data)

# counting unique values
for column in data.columns:
    print(f"Uniques for {column}: {data[column].unique()}")

# format of each column
for column in data.columns:
    print(f"Format for {column}: {type(data[column][0])}")

# finding null values
print(data.isna().sum())
# cleaning null values
data['Age'] = data['Age'].fillna(method="ffill")
print(data.isna().sum())

# transforming data
print(data['Age'].unique())
print(data['Name'].unique())
print(data['BHK'].unique())

data['BHK'] = data['BHK'].apply(lambda x: int(x.split()[0]))

print("\nCleaned data:")
print(data)


