# Write a program to do: A dataset collected in a cosmetics shop showing details of customers and 
# whether or not they responded to a special offer to buy a new lip-stick is shown in table below. 
# (Use library commands)
# According to the decision tree you have made from the previous training
# data set, what is the decision for the test data: 
# [Age > 35, Income = Medium, Gender = Female, Marital Status = Married]?

dataset: dict[str:list] = {
    'Id':               [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    'Age':              ['<21','<21','21-35','>35','>35','>35','21-35','<21','<21','>35','<21','21-35','21-35','>35'],
    'Income':           ['High','High','High','Medium','Low','Low','Low','Medium','Low','Medium','Medium','Medium','High','Medium'],
    'Gender':           ['Male','Male','Male','Male','Female','Female','Female','Male','Female','Female','Female','Male','Female','Male'],
    'MaritalStatus':    ['Single','Married','Single','Single','Single','Married','Married','Single','Married','Single','Married','Married','Single','Married'],
    'Buys':             ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = pd.DataFrame(dataset)
data = data.drop('Id', axis=1)
print("Describing: ")
print(data.describe())
print()

le = LabelEncoder()
x = data.iloc[:, :-1] # excluding last column and taking all the rows and columns
x = x.apply(le.fit_transform)
print("Encoded data:")
print(x)
print()

y = data.iloc[:, -1] # storing labels in y
print(y)
classifier = DecisionTreeClassifier(criterion='entropy')
classifier.fit(x, y)

test_x = np.array([2,2,0,0])
pred_y = classifier.predict([test_x])
print(pred_y)
