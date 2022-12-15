# Use the dataset 'titanic'. The dataset contains 891 rows and 
# contains information about the passengers who boarded the unfortunate Titanic ship. 
# Use the Seaborn library to see if we can find any patterns in the data.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

data = sns.load_dataset('titanic')
print(data)
print()

# shape of data
print(data.shape)
print()

sns.lineplot(data['age'])
plt.show()

sns.displot(data['age'])
plt.show()

sns.distplot(data['age'], hist=False)
plt.show()

sns.distplot(data['age'])
plt.show()

sns.relplot(x='age', y='fare', col='pclass', hue='sex', style='sex', kind='line', data=data)
plt.show()

sns.scatterplot(x='age', y='fare', hue='sex', data=data)
plt.show()

sns.lineplot(x='age', y='fare', style='sex', hue='sex', data=data)
plt.show()

sns.barplot(x='sex', y='survived', hue='pclass', data=data)
plt.show()

sns.stripplot(x='sex', y='age', data=data)
plt.show()

sns.swarmplot(x='sex', y='age', data=data)
plt.show()

sns.boxplot(x='survived', y='age', data=data)
plt.show()

sns.boxplot(x='survived', y='age', hue='sex', data=data)
plt.show()