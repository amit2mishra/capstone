#!/usr/bin/env python
# coding: utf-8

# <h1> Getting the Neighbourhood </h1>

# In[8]:


#importing all the required libraries

import requests
import lxml.html as lh
import bs4 as bs
import urllib.request
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


#!pip install shapely
#!pip install geopandas


# In[9]:


from shapely.geometry import Point
import geopandas as gpd


# In[10]:


#Getting the data from url in html tables
url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
res = requests.get(url)
soup = bs.BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
data = pd.read_json(df[0].to_json(orient='records'))


# In[11]:


data.head()


# In[12]:


#Choosing only data where field Borough doesn't have not assigned value
raw_data_selected = data[data['Borough'] != 'Not assigned']


# In[18]:


#Grouping Data
raw_data_selected = raw_data_selected.groupby(['Postal Code', 'Borough'], as_index=False).agg(','.join)


# In[19]:


raw_data_selected.head()


# In[20]:


#Replacing values in Neighbourhood field with Borough where Neighbourhood is not assigned
raw_data_selected['Neighbourhood'] = np.where(raw_data_selected['Neighbourhood'] == 'Not assigned', raw_data_selected['Borough'], raw_data_selected['Neighbourhood'])


# In[21]:


#Shape of Data
raw_data_selected.shape

