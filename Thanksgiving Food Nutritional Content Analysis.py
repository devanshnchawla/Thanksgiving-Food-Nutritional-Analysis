#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define function to retrieve nutrient values for a food
def get_nutrient_values(food):
    #url is hidden because of key, source: https://api.nal.usda.gov/fdc/v1/foods/
    response = requests.get(url)
    data = response.json()

    nutrients = data['foods'][0]['foodNutrients']
    energy = 0
    carbs = 0
    protein = 0
    fiber = 0
    fat = 0

    for nutrient in nutrients:
        if nutrient['nutrientName'] == 'Energy':
            energy = nutrient['value']
        elif nutrient['nutrientName'] == 'Carbohydrate, by difference':
            carbs = nutrient['value']
        elif nutrient['nutrientName'] == 'Protein':
            protein = nutrient['value']
        elif nutrient['nutrientName'] == 'Fiber, total dietary':
            fiber = nutrient['value']
        elif nutrient['nutrientName'] == 'Total lipid (fat)':
            fat = nutrient['value']

    return {'Energy (kcal)': energy, 'Carbs (g)': carbs, 'Protein (g)': protein, 'Fiber (g)': fiber, 'Fat (g)': fat}

# Define list of Thanksgiving dinner foods
thanksgiving_foods = ['turkey', 'macaroni and cheese', 'mashed potatoes', 'bread stuffing', 'ham', 'sweet potato souffle', 'cranberry sauce', 'mixed vegetables', 'apple pie', 'pecan pie']

# Create dictionary of nutrient values for each food
nutrient_dict = {}
for food in thanksgiving_foods:
    nutrient_dict[food] = get_nutrient_values(food)

# Create pandas dataframe from dictionary
df = pd.DataFrame(nutrient_dict).transpose()

# Display dataframe
df.head(10)


# In[13]:


plt.scatter(df['Protein (g)'], df['Energy (kcal)'])
plt.title('Association between Protein and Energy in Thanksgiving Foods')
plt.xlabel('Protein (g)')
plt.ylabel('Energy (kcal)')
plt.show()


# In[11]:


# Define function to create bar graph for a single nutrient
def plot_nutrient(nutrient):
    plt.figure(figsize=(10,6)) # increase figure size
    plt.bar(df.index, df[nutrient], width=0.5) # increase bar width
    plt.title(f'{nutrient} Content in Thanksgiving Foods')
    plt.xlabel('Food')
    plt.ylabel(f'{nutrient} ({df[nutrient].iloc[0]} Units)')
    plt.xticks(rotation=45, ha='right') # rotate x-axis labels for better readability
    plt.show()

# Create bar graphs for each nutrient
plot_nutrient('Energy (kcal)')
plot_nutrient('Carbs (g)')
plot_nutrient('Protein (g)')
plot_nutrient('Fiber (g)')
plot_nutrient('Fat (g)')


# In[ ]:




