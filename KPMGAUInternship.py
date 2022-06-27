#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #Data Preparation


# In[2]:


import numpy as np #Linear Algebra


# In[3]:


dff= pd.read_excel(r"C:\Users\acer\OneDrive\Desktop\Datasets\KPMG_VI_New_raw_data_update_final.xlsx", sheet_name='Transactions')


# In[4]:


dff.shape


# In[5]:


dff.isnull().sum()


# In[7]:


dff['online_order']=dff['online_order'].fillna('No Online Order Specified')


# In[8]:


dff['brand']= dff['brand'].fillna('No Brand Specified')


# In[9]:


dff['product_line']= dff['product_line'].fillna('No Product Line Specified')


# In[10]:


dff['product_class']=dff['product_class'].fillna('No Product Class Specified')


# In[11]:


dff['product_size']=dff['product_size'].fillna('No Product Size Specified')


# In[12]:


dff['standard_cost']=dff['standard_cost'].fillna('No Standard Cost Specified')


# In[5]:


dff['product_first_sold_date']=dff['product_first_sold_date'].fillna('No Product Sold Date Specified')


# In[6]:


dff['product_first_sold_date']= pd.to_datetime(dff['product_first_sold_date']).dt.date


# In[14]:


dff.head()


# In[15]:


dff.isnull().sum()


# In[15]:


dff['online_order'].value_counts()


# In[16]:


dff.describe()


# In[17]:


dff.columns


# In[18]:


dff['order_status'].value_counts()


# In[19]:


dff['brand'].value_counts()


# In[13]:


dff.info()


# In[23]:


dup=dff.duplicated()
dff[dup].sum()


# In[60]:


dff1= pd.read_excel(r"C:\Users\acer\OneDrive\Desktop\Datasets\KPMG_VI_New_raw_data_update_final.xlsx", sheet_name='CustomerDemographic')


# In[61]:


dff1.head(20)


# In[70]:


dff1['gender'].value_counts()


# In[63]:


dff1['gender'].str.replace('U','Undefined')


# In[69]:


dff1['gender'] = df['gender'].replace(['F'],'Female').replace(['U'],'Undefined').replace(['Femal'],'Female').replace(['M'],'Male')


# In[71]:


dff1.isnull().sum()


# In[74]:


dff1= dff1.drop('default', axis=1)


# In[75]:


dff1.head()


# In[76]:


dff1.describe()


# In[77]:


dff1.duplicated().sum()


# In[79]:


dff2= pd.read_excel(r"C:\Users\acer\OneDrive\Desktop\Datasets\KPMG_VI_New_raw_data_update_final.xlsx", sheet_name='NewCustomerList')


# In[80]:


dff2.head()


# In[81]:


dff2.columns


# In[82]:


dff2.isnull().sum()


# In[83]:


cols=['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20']


# In[86]:


dff2.drop(cols, axis=1, inplace=True)


# In[87]:


dff2.head()


# In[88]:


dff2.describe()


# In[90]:


dff2.duplicated().sum()


# In[91]:


dff1.head()


# In[112]:


filter= dff1[(dff1['DOB'] < '1920-01-01')]


# In[111]:


dff1.drop([33], axis=0, inplace=True)


# In[ ]:




