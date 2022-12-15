# With reference to Table, obtain the Frequency table for the attribute age. 
# From the frequency table you have obtained, calculate the information gain of the frequency table while splitting on Age. 
# (Use step by step Python/Pandas commands)

dataset = {
    "Age": ["Young", "Young", "Middle", "Old", "Old", "Old", "Middle", "Young", "Young", "Old", "Young", "Middle", "Middle", "Old"],
    "Income": ["High", "High", "High", "Medium", "Low", "Low", "Low", "Medium", "Low", "Medium", "Medium", "Medium", "High", "Medium"],
    "Married": ["No", "No", "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "No"],
    "Health": ["Fair", "Good", "Fair","Fair","Fair", "Good",  "Good", "Fair","Fair","Fair", "Good",  "Good", "Fair", "Good"],
    "Class": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
}

import pandas as pd
data = pd.DataFrame(dataset)

print(data['Age'].value_counts())