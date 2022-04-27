# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:30:02 2022

@author: 
"""

import json 
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

mydb = client["Supermarket"]
mycollection = mydb["Sales"]

with open('C://Users//Deep.ai//Downloads//Supermarket sales.json') as file:
    data = json.load(file)


if isinstance(data, list):
    mycollection.insert_many(data)
else:
    mycollection.insert_one(data)


mydata = mydb.Sales

import pandas as pd 
df = pd.DataFrame(list(mydata.find()))



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df['Date']=pd.to_datetime(df['Date'])

df['weekday']=df['Date'].dt.day_name()
df.head()

df.describe()

#What does the customer rating look like and is it skewed?
sns.distplot(df['Rating'])
plt.axvline(x=df['Rating'].mean(),c='red',ls='--',label= 'mean')
plt.axvline(x=np.percentile(df['Rating'],25),c='yellow',ls='--',label ='25th percentile:Q1')
plt.axvline(x=np.percentile(df['Rating'],75),c='green',ls='--',label ='75th percentile:Q3')
plt.legend(loc='upper right')

print("sum of null values ",df.isna().sum())
#Q2: Is there any difference in aggregate sales across branches?
sns.countplot(df['Branch'],palette = 'magma')


#Type of customers : normal or member?

sns.countplot(df['Customer type'])

#Which is the most pouplar payment method used by customers?
sns.countplot(df['Payment'])



sns.regplot(x=df['Rating'],y= df['gross income'])

#What is the relationship between Gender and Gross income?
sns.boxplot(df['Gender'],df['gross income'])


################################################

plt.figure(figsize = (15,8))

sns.boxplot(df['Product line'],df['gross income'])
plt.show()

# Sending the data to 

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
  
  
#conn_string = 'postgres://postgres:1234@127.0.0.1/Sales_data'
  

import sqlalchemy  # Package for accessing SQL databases via Python

# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine("postgres://postgres:1234@127.0.0.1/Sales_data")
con = engine.connect()

# Verify that there are no existing tables
print(engine.table_names())


table_name = 'Sales_2_data'
df.to_sql(table_name, con)

print(engine.table_names())
con.close()




