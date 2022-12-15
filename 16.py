# Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
# contains information about the passengers who boarded the unfortunate Titanic ship. 
# Write a code to check how the price of the ticket 
# (columnname: 'fare') for each passenger is distributed by plotting a histogram.

import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('titanic')
print(data)
print()

sns.relplot(data=data, y='fare', x='sex', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='pclass', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='age', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='parch', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='sibsp', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='embarked', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='class', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='who', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='deck', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='embark_town', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='alive', size='fare', hue='fare')
sns.relplot(data=data, y='fare', x='alone', size='fare', hue='fare')
plt.show()

sns.displot(data=data, x='fare', hue='sex')
sns.displot(data=data, x='fare', hue='pclass')
sns.displot(data=data, x='fare', hue='age')
sns.displot(data=data, x='fare', hue='parch')
sns.displot(data=data, x='fare', hue='sibsp')
sns.displot(data=data, x='fare', hue='embarked')
sns.displot(data=data, x='fare', hue='class')
sns.displot(data=data, x='fare', hue='who')
sns.displot(data=data, x='fare', hue='deck')
sns.displot(data=data, x='fare', hue='embark_town')
sns.displot(data=data, x='fare', hue='alive')
sns.displot(data=data, x='fare', hue='alone')
plt.show()

sns.histplot(data=data['fare'])
plt.show()

