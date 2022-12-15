# Write a program to do: 
# A dataset collected in a cosmetics shop showing details of customers and 
# whether or not they responded to a special offer to buy a new lip-stick is shown in table below. 
# (Implement step by step using commands - Dont use library) 
# Use this dataset to build a decision tree, with Buys as the target variable, to help in buying lipsticks in the
# future. Find the root node of the decision tree.

dataset: dict[str:list] = {
    'Id':               [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    'Age':              ['<21','<21','21-35','>35','>35','>35','21-35','<21','<21','>35','<21','21-35','21-35','>35'],
    'Income':           ['High','High','High','Medium','Low','Low','Low','Medium','Low','Medium','Medium','Medium','High','Medium'],
    'Gender':           ['Male','Male','Male','Male','Female','Female','Female','Male','Female','Female','Female','Male','Female','Male'],
    'MaritalStatus':    ['Single','Married','Single','Single','Single','Married','Married','Single','Married','Single','Married','Married','Single','Married'],
    'Buys':             ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}
columns = ['Id', 'Age', 'Income', 'Gender', 'MaritalStatus', 'Buys']

import math
import pandas as pd

data = pd.DataFrame(dataset)

n = data["Buys"].__len__()

def entropyS():
    yes = data.loc[data['Buys'] == 'Yes'].__len__()
    no = data.loc[data['Buys'] == 'No'].__len__()
    Py = yes / n
    Pn = no / n
    return -Py * math.log2(Py) - Pn * math.log2(Pn)


def informationGainMaritalStatus():
    single = data.loc[data['MaritalStatus'] == 'Single']
    nSingle = single.__len__()
    yesSingle = single.loc[data['Buys'] == 'Yes'].__len__()
    noSingle = single.loc[data['Buys'] == 'No'].__len__()
    PySingle = yesSingle / nSingle
    PnSingle = noSingle / nSingle
    entropySingle = -PySingle * math.log2(PySingle) - PnSingle * math.log2(PnSingle)

    married = data.loc[data['MaritalStatus'] == 'Married']
    nMarried = married.__len__()
    yesMarried = married.loc[data['Buys'] == 'Yes'].__len__()
    noMarried = married.loc[data['Buys'] == 'No'].__len__()
    PyMarried = yesMarried / nMarried
    PnMarried = noMarried / nMarried
    entropyMarried = -PyMarried * math.log2(PyMarried) - PnMarried * math.log2(PnMarried)

    information = entropySingle * (nSingle / n) + entropyMarried * (nMarried / n)
    gain = entropy - information
    return gain


def informationGainGender():
    male = data.loc[data['Gender'] == 'Male']
    nMale = male.__len__()
    yesMale = male.loc[data['Buys'] == 'Yes'].__len__()
    noMale = male.loc[data['Buys'] == 'No'].__len__()
    PyMale = yesMale / nMale
    PnMale = noMale / nMale
    entropyMale = -PyMale * math.log2(PyMale) - PnMale * math.log2(PnMale)

    female = data.loc[data['Gender'] == 'Female']
    nFemale = female.__len__()
    yesFemale = female.loc[data['Buys'] == 'Yes'].__len__()
    noFemale = female.loc[data['Buys'] == 'No'].__len__()
    PyFemale = yesFemale / nFemale
    PnFemale = noFemale / nFemale
    entropyFemale = -PyFemale * math.log2(PyFemale) - PnFemale * math.log2(PnFemale)

    information = entropyMale * (nMale / n) + entropyFemale * (nFemale / n)
    gain = entropy - information
    return gain


def informationGainIncome():
    high = data.loc[data['Income'] == 'High']
    nHigh = high.__len__()
    yesHigh = high.loc[data['Buys'] == 'Yes'].__len__()
    noHigh = high.loc[data['Buys'] == 'No'].__len__()
    PyHigh = yesHigh / nHigh
    PnHigh = noHigh / nHigh
    entropyHigh = -PyHigh * math.log2(PyHigh) - PnHigh * math.log2(PnHigh)

    medium = data.loc[data['Income'] == 'Medium']
    nMedium = medium.__len__()
    yesMedium = medium.loc[data['Buys'] == 'Yes'].__len__()
    noMedium = medium.loc[data['Buys'] == 'No'].__len__()
    PyMedium = yesMedium / nMedium
    PnMedium = noMedium / nMedium
    entropyMedium = -PyMedium * math.log2(PyMedium) - PnMedium * math.log2(PnMedium)

    low = data.loc[data['Income'] == 'Low']
    nLow = low.__len__()
    yesLow = low.loc[data['Buys'] == 'Yes'].__len__()
    noLow = low.loc[data['Buys'] == 'No'].__len__()
    PyLow = yesLow / nLow
    PnLow = noLow / nLow
    entropyLow = -PyLow * math.log2(PyLow) - PnLow * math.log2(PnLow)

    information = entropyHigh * (nHigh / n) + entropyMedium * (nMedium / n) + entropyLow * (nLow / n)
    gain = entropy - information
    return gain


def informationGainAge():
    high = data.loc[data['Age'] == '>35']
    nHigh = high.__len__()
    yesHigh = high.loc[data['Buys'] == 'Yes'].__len__()
    noHigh = high.loc[data['Buys'] == 'No'].__len__()
    PyHigh = yesHigh / nHigh
    PnHigh = noHigh / nHigh
    entropyHigh = -PyHigh * math.log2(PyHigh) - PnHigh * math.log2(PnHigh)

    medium = data.loc[data['Age'] == '21-35']
    nMedium = medium.__len__()
    yesMedium = medium.loc[data['Buys'] == 'Yes'].__len__()
    noMedium = medium.loc[data['Buys'] == 'No'].__len__()
    PyMedium = yesMedium / nMedium
    PnMedium = noMedium / nMedium
    entropyMedium = 0 if PyMedium == 0 or PnMedium == 0 else -PyMedium * math.log2(PyMedium) - PnMedium * math.log2(PnMedium)

    low = data.loc[data['Age'] == '<21']
    nLow = low.__len__()
    yesLow = low.loc[data['Buys'] == 'Yes'].__len__()
    noLow = low.loc[data['Buys'] == 'No'].__len__()
    PyLow = yesLow / nLow
    PnLow = noLow / nLow
    entropyLow = -PyLow * math.log2(PyLow) - PnLow * math.log2(PnLow)

    information = entropyHigh * (nHigh / n) + entropyMedium * (nMedium / n) + entropyLow * (nLow / n)
    gain = entropy - information
    return gain


entropy = entropyS()
igAge = informationGainAge()
igIncome = informationGainIncome()
igGender = informationGainGender()
igMaritalStatus = informationGainMaritalStatus()

maxInformationGain = max(igMaritalStatus, igGender, igIncome, igAge)
head = 1 if maxInformationGain == igAge else 2 if maxInformationGain == igIncome else 3 if maxInformationGain == igGender else 4
print(f"Head of the Decision Tree is {columns[head]}")
