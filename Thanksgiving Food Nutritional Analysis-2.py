#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import matplotlib.pyplot as plt

# API parameters
#api key hidden
query = "turkey,macaroni and cheese,mashed potatoes,bread stuffing,ham,sweet potato souffle,cranberry sauce,mixed vegetables,apple pie,pecan pie"

# Send GET request to FDC API
response = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={query}")

# Get list of foods from response
foods = response.json()["foods"]

# Create dictionary to store nutrient information
nutrients = {"Energy": [], "Carbohydrate": [], "Protein": [], "Fiber": [], "Fat": []}

# Loop through foods and extract nutrient information
for food in foods:
    nutrient_info = food["foodNutrients"]
    for nutrient in nutrients.keys():
        nutrient_value = [info["value"] for info in nutrient_info if info["nutrientName"] == nutrient]
        if len(nutrient_value) > 0:
            nutrient_avg = sum(nutrient_value) / len(nutrient_value)
        else:
            nutrient_avg = 0
        nutrients[nutrient].append(nutrient_avg)

# Create dataframe from dictionary of nutrient information
df_nutrients = pd.DataFrame(nutrients, index=[food["description"] for food in foods])

# Create scatter plot of protein vs energy
plt.scatter(df_nutrients["Energy"], df_nutrients["Protein"])
plt.title("Association between Protein and Energy in Thanksgiving Foods")
plt.xlabel("Energy (kcal)")
plt.ylabel("Protein (g)")
plt.show()

# Create bar graphs for each nutrient
for nutrient in nutrients.keys():
    plt.bar(df_nutrients.index, df_nutrients[nutrient])
    plt.title(f"{nutrient} Content in Thanksgiving Foods")
    plt.xlabel("Food")
    plt.xticks(rotation=90)
    plt.ylabel(f"{nutrient} (g)")
    plt.show()


# In[4]:


df_nutrients.head(10)


# In[ ]:




