#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
get_ipython().system('pip install kaggle')


# In[3]:


# Download dataset from Kaggle
import kaggle
get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[6]:


#extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


# In[8]:


#read the data from the file and handle null values
import pandas as pd
df = pd.read_csv('orders.csv', na_values = ['Not Available', 'unknown'])
df['Ship Mode'].unique()


# In[13]:


#Rename column names to lower case and to include underscores
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')


# In[19]:


# Derive new columns discount, sale price and profit
df['discount'] = df['list_price'] * df['discount_percent']*.01
df['sale_price']= df['list_price'] - df['discount']
df['profit']=df['sale_price'] - df['cost_price']


# In[20]:


df.columns


# In[22]:


# Convert order date from object data type to datetime
df['order_date'] = pd.to_datetime(df['order_date'], format = "%Y-%m-%d")


# In[24]:


df.dtypes


# In[25]:


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[27]:


#load the data into sql server using replace option
import sqlalchemy as sal
engine = sal.create_engine('mssql://DESKTOP-I6H41H1\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[29]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')

