# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 01:57:29 2022

@author: Deep.ai
"""

import json 
from pymongo import MongoClient
import plotly.express as px


client = MongoClient("mongodb://localhost:27017/")

mydb = client["E-Commerce"]
mycollection = mydb["Shipping"]

with open('C://Users//Deep.ai//Downloads//E-Commerce Shipping Data.json') as file:
    data = json.load(file)


if isinstance(data, list):
    mycollection.insert_many(data)
else:
    mycollection.insert_one(data)


mydata = mydb.Shipping


import pandas as pd 
df = pd.DataFrame(list(mydata.find()))

print("Shape of data",df.shape)

# Descriptive analysis of data 
print("Descriptive of Data ",)
print(df.describe)

print("Caluating the null values ")
print(df.isnull().sum())


df.drop('ID', axis = 1, inplace = True)
df.head()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(18, 7))
sns.heatmap(df.corr(), annot=True, linewidth=5, linecolor='white')

plt.figure(figsize = (15, 7))
ax = sns.distplot(df['Discount_offered'], color = 'y')

plt.show()



# creating a list of categorical coumns
cols = ['Warehouse_block', 'Mode_of_Shipment', 'Customer_care_calls', 'Customer_rating',
        'Prior_purchases', 'Product_importance', 'Gender', 'Reached.on.Time_Y.N']

plt.figure(figsize = (16, 20))
plotnumber = 1

# plotting the countplot of each categorical column.

for i in range(len(cols)):
    if plotnumber <= 8:
        ax = plt.subplot(4, 2, plotnumber)
        sns.countplot(x = cols[i], data = df, ax = ax, palette='rocket')
        plt.title(f"\n{cols[i]} Value Counts\n", fontsize = 20)
        
    plotnumber += 1

plt.tight_layout()
plt.show()

#####################################

# looking at the gender column and what are the categories present in it
object_columns = df.select_dtypes(include = ['object'])

gender = object_columns['Gender'].value_counts().reset_index()
gender.columns = ['Gender', 'value_counts']
fig = px.pie(gender, names = 'Gender', values = 'value_counts', color_discrete_sequence = 
            px.colors.sequential.Darkmint_r, width = 650, height = 400, hole = 0.5)
fig.update_traces(textinfo = 'percent+label')


##################################################


sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(x=df.Warehouse_block,y=df.Cost_of_the_Product,hue=df.Product_importance).set_title("Cost_of_the_Product VS Warehouse_block BarPlot On the basis of Product Importance")


################################################################
adult_dict = df.to_dict('records') 

from pymongo import MongoClient

data_base = client["Ecomm_cleaned"]
user_info_table = data_base["Ship_cleaned"]
user_info_table.insert_many(adult_dict)