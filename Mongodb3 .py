#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
import json
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#making connection with mongodb installed in localhost
mongoclientdb = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = mongoclientdb["supermarket"]
colldb = mydb["market"]


# In[3]:


#uploading the dataset in mongodb 
with open("H:\\supermarketsales.json") as f:
    data = json.load(f)


colldb.insert_many(data)


# In[4]:


#storing data in variable
my_data =mydb.market


# In[5]:


df = pd.DataFrame(list(my_data.find()))


# In[6]:


#displaying dataset 
df.head()


# In[7]:


#changing data type Date in datetime
df['date'] = pd.to_datetime(df['Date'])


# In[8]:


df['date'] = pd.to_datetime(df['date'])


# In[9]:


df['day'] = (df['date']).dt.day
df['month'] = (df['date']).dt.month
df['year'] = (df['date']).dt.year


# In[10]:


df['Time'] = pd.to_datetime(df['Time'])


# In[11]:


df['Hour'] = (df['Time']).dt.hour


# In[12]:


#gender count
sns.set(style="darkgrid")
countGender  = sns.countplot(x="Gender", data =df).set_title("Gender_Count")


# In[13]:


#rating of branches
sns.boxplot(x="Branch", y = "Rating" ,data =df).set_title("Ratings by Branch")


# In[14]:


#product sales per hour iin the company
countGender  = sns.lineplot(x="Hour",  y = 'Quantity',data =df).set_title("Product Sales per Hour")


# In[15]:


#each branch sale in by hour in monthly fashion
countGender  = sns.relplot(x="Hour",  y = 'Total', col= 'month' , row= 'Branch', estimator = None, kind="line", data =df)


# In[16]:


#product performance
sns.boxenplot(y = 'Product line', x = 'Quantity', data=df )


# In[17]:


#product sales in various branches
countProd  = sns.relplot(x="Hour",  y = 'Quantity', col= 'Product line' , row= 'Branch', estimator = None, kind="line", data =df)


# In[18]:


#payment type distribution across all branches
sns.countplot(x="Payment", hue = "Branch", data =df).set_title("Payment Channel by Branch") 


# In[19]:


#Saving data
marketData = df.to_dict('records')
newdb = mongoclientdb["NewSuperMarketData"]
mydata = newdb["supMarket"]
mydata.insert_many(marketData)


# In[ ]:




