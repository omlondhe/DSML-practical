# Perform the following operations using Python on a data set :
# read data from different formats(like csv, xls), indexing and selecting data, sort data,
# describe attributes of data, checking data types of each column. 
# (Use Titanic Dataset).

import pandas as pd

# index_col is making PassengerId as index to use .loc[] like functions using that Primary key for targeting
data = pd.read_csv('01.csv', index_col="PassengerId")
print("Columns")
print(data.columns)
print()

# Indexing is called as Subset selection

# Selecting using []
# Selecting single column
print("Selecting single column")
print(data["Name"])
print()

# Selecting multiple columns
print("Selecting multiple column")
print(data[["Name", "Survived"]])
print()


# Selecting using .loc[] 
# Selecting single column
print("Selecting single column")
print(data.loc[892])
print()

# Selecting multiple columns
print("Selecting multiple column")
print(data.loc[[892, 893, 894]])
print()

# Selecting multiple rows and some columns
print("Selecting multiple column")
print(data.loc[[892, 893, 894], ["Name", "Age"]])
print()
