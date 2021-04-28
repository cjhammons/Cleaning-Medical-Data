#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install pandas')
get_ipython().system('pip install scipy')
get_ipython().system('pip install sklearn')


# In[36]:


import numpy as np
import pandas as pd
from pandas import DataFrame
import scipy.stats as stats
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA


# # Data Inspection

# In[3]:


medical_raw = pd.read_csv('medical_raw_data.csv')
medical_raw.info()


# The first thing we notice is the columns of the dataset follow the naming convention of using underscores between words... except for TotalCharge, which simply capitalizes the second word. We'll fix this inconsistency before we move forward.

# In[4]:


medical_raw.rename(columns = {'TotalCharge': 'Total_charge'}, inplace=True)
medical_raw[['Total_charge']]


# # Handling Null Values
# 
# Let's check which columns contain null values:

# In[5]:


medical_raw.isnull().any()


# Upon inspection we find that the following columns contain null values:
#     
# - Children
# - Age
# - Income
# - soft_drink
# - Overweight
# - Anxiety
# - Initial_days

# ## Children
# For the Children column, we will use ``fillna()`` from pandas specifying ``method='bfill'`` to fill in the missing data based on the data that is not null. 

# In[6]:


medical_raw['Children'].fillna(method='bfill', inplace=True)


# Check if there are any null values remaining:

# In[7]:


medical_raw['Children'].isna().sum()


# ## Age

# In[8]:


medical_raw['Age'].isna().sum()


# We'll use the same methodology for Age that we used for Children previously.

# In[9]:


medical_raw['Age'].fillna(round(medical_raw['Age'].mean()), inplace=True)


# Check if there are any null values remaining:

# In[10]:


medical_raw['Age'].isna().sum()


# ## Income

# In[11]:


medical_raw['Income'].isna().sum()


# For Income we will replace the null values with the mean of the given values.

# In[12]:


income_mean = medical_raw['Income'].mean()
income_mean


# In[13]:


medical_raw['Income'].fillna(medical_raw['Income'].mean(), inplace=True)


# In[14]:


medical_raw['Income'].isna().sum()


# ## Soft_drink

# In[15]:


medical_raw['Soft_drink'].isna().sum()


# Since soft_drink is categorical, either a "Yes" or "No", we'll replace the nulls with the mode.

# In[16]:


medical_raw['Soft_drink'].fillna(medical_raw['Soft_drink'].mode()[0], inplace=True)
medical_raw['Soft_drink'].isnull().sum()


# ## Overweight

# In[17]:


medical_raw['Overweight'].isna().sum()


# Overweight is also categorical, though it is "0" and "1" instead of "yes and "no" (we'll fix these inconsitencies in the categorical values later). We'll use the same method we used for soft_drink.

# In[18]:


medical_raw['Overweight'].fillna(medical_raw['Overweight'].mode()[0], inplace=True)
medical_raw['Overweight'].isna().sum()


# ## Anxiety
# Another categorical! we use mode again

# In[19]:


medical_raw['Anxiety'].isna().sum()


# In[20]:


medical_raw['Anxiety'].fillna(medical_raw['Anxiety'].mode()[0], inplace=True)
medical_raw['Anxiety'].isna().sum()


# ## Initial_days
# Numerical

# In[21]:


medical_raw['Initial_days'].isna().sum()


# In[22]:


medical_raw['Initial_days'].fillna(medical_raw['Initial_days'].mean(), inplace=True)
medical_raw['Initial_days'].isna().sum()


# In[23]:


medical_raw.isnull().any()


# In[24]:


medical_raw.to_csv('clean.csv')


# # Handling Outliers

# Now we'll check all of the numeric data fields for outliers and handle them if needed.

# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Z-scores
# We're going to add a column to the dataset for each numeric feature that contains a standardized z-score. We'll leave the original columns unaltered so the original data are still accessible. 

# In[26]:


medical_raw['Zscore_Population'] = stats.zscore(medical_raw['Population'])
medical_raw['Zscore_Children'] = stats.zscore(medical_raw['Children'])
medical_raw['Zscore_Age'] = stats.zscore(medical_raw['Age'])
medical_raw['Zscore_Income'] = stats.zscore(medical_raw['Income'])
medical_raw['Zscore_Doc_visits'] = stats.zscore(medical_raw['Doc_visits'])
medical_raw['Zscore_Full_meals_eaten'] = stats.zscore(medical_raw['Full_meals_eaten'])
medical_raw['Zscore_Initial_days'] = stats.zscore(medical_raw['Initial_days'])
medical_raw['Zscore_Total_charge'] = stats.zscore(medical_raw['Total_charge'])
medical_raw['Zscore_Additional_charges'] = stats.zscore(medical_raw['Additional_charges'])


# In[27]:


medical_raw['Zscore_Population'].plot.box()


# In[28]:


medical_raw['Zscore_Children'].plot.box()


# In[29]:


medical_raw['Zscore_Age'].plot.box()


# In[30]:


medical_raw['Zscore_Income'].plot.box()


# In[31]:


medical_raw['Zscore_Doc_visits'].plot.box()


# In[32]:


medical_raw['Zscore_Full_meals_eaten'].plot.box()


# In[33]:


medical_raw['Zscore_Initial_days'].plot.box()


# In[34]:


medical_raw['Zscore_Total_charge'].plot.box()


# In[35]:


medical_raw['Zscore_Additional_charges'].plot.box()


# # Principle Component Analysis

# In[42]:


# adapted from "Data Science Foundations: Data Mining" chapter 2 section 4
X = medical_raw[['Zscore_Population', 'Zscore_Children', 'Zscore_Age', 
                 'Zscore_Income', 'Zscore_Doc_visits', 'Zscore_Full_meals_eaten', 
                 'Zscore_Initial_days', 'Zscore_Total_charge', 'Zscore_Additional_charges']]


# In[43]:


pca = PCA()
pca.fit(X)
print(pca.explained_variance_ratio_)


# In[44]:


print(pca.components_)

