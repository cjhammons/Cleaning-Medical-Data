#!/usr/bin/env python
# coding: utf-8

# In[1]:

'''
get_ipython().system('pip install numpy')
get_ipython().system('pip install pandas')
get_ipython().system('pip install scipy')
get_ipython().system('pip install sklearn')
get_ipython().system('pip install matplotlib')
'''

# In[2]:


import numpy as np
import pandas as pd
from pandas import DataFrame
import scipy.stats as stats
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# # Data Inspection

# In[3]:


medical_raw = pd.read_csv('data/medical_raw_data.csv')
medical_raw.info()
medical_raw.head()


# The first thing we notice is the columns of the dataset follow the naming convention of using underscores between words except for three outliers: TotalCharge, BackPain, HighBlood, and ReAdmis, which simply capitalizes the second word. We'll fix this inconsistency before we move forward.

# In[4]:


medical_raw.rename(columns = {
    'CaseOrder': 'Case_order',
    'TotalCharge': 'Total_charge',
    'BackPain': 'Back_pain',
    'HighBlood': 'High_blood',
    'ReAdmis': 'Re_admis'
}, inplace=True)


# We're also going to drop the useless index column.

# In[5]:


medical_raw.drop(['Unnamed: 0'], axis=1, inplace=True)


# # Handling Null Values
# 
# Let's check which columns contain null values:

# In[6]:


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
# For the Children column, we will use ``fillna()`` and ``mean()`` to fill the null values with the mean of the existing values

# In[7]:


medical_raw['Children'].fillna(round(medical_raw['Children'].mean()), inplace=True)


# Check if there are any null values remaining:

# In[8]:


medical_raw['Children'].isna().sum()


# ## Age

# In[9]:


medical_raw['Age'].isna().sum()


# We'll use the same methodology for Age that we used for Children previously.

# In[10]:


medical_raw['Age'].fillna(round(medical_raw['Age'].mean()), inplace=True)


# Check if there are any null values remaining:

# In[11]:


medical_raw['Age'].isna().sum()


# ## Income

# In[12]:


medical_raw['Income'].isna().sum()


# For Income we will replace the null values with the mean of the given values.

# In[13]:


income_mean = medical_raw['Income'].mean()
income_mean


# In[14]:


medical_raw['Income'].fillna(medical_raw['Income'].mean(), inplace=True)


# In[15]:


medical_raw['Income'].isna().sum()


# ## Soft_drink

# In[16]:


medical_raw['Soft_drink'].isna().sum()


# Since soft_drink is categorical, either a "Yes" or "No", we'll replace the nulls with the mode.

# In[17]:


medical_raw['Soft_drink'].fillna(medical_raw['Soft_drink'].mode()[0], inplace=True)
medical_raw['Soft_drink'].isnull().sum()


# ## Overweight

# In[18]:


medical_raw['Overweight'].isna().sum()


# Overweight is also categorical, though it is "0" and "1" instead of "yes and "no" we'll fix this inconsistency as well. We'll use the same method we used for soft_drink.

# In[19]:


medical_raw['Overweight'].fillna(medical_raw['Overweight'].mode()[0], inplace=True)
medical_raw['Overweight'].isna().sum()


# In[20]:


medical_raw['Overweight'] = medical_raw['Overweight'].replace(1, "Yes")
medical_raw['Overweight'] = medical_raw['Overweight'].replace(0, "No")


# ## Anxiety
# Another categorical! we use mode again

# In[21]:


medical_raw['Anxiety'].isna().sum()


# In[22]:


medical_raw['Anxiety'].fillna(medical_raw['Anxiety'].mode()[0], inplace=True)
medical_raw['Anxiety'].isna().sum()


# In[23]:


medical_raw['Anxiety'] = medical_raw['Overweight'].replace(1, "Yes")
medical_raw['Anxiety'] = medical_raw['Overweight'].replace(0, "No")


# ## Initial_days
# Numerical

# In[24]:


medical_raw['Initial_days'].isna().sum()


# In[25]:


medical_raw['Initial_days'].fillna(medical_raw['Initial_days'].mean(), inplace=True)
medical_raw['Initial_days'].isna().sum()


# In[26]:


medical_raw.isnull().any()


# In[ ]:





# # Handling Outliers

# Now we'll check all of the numeric data fields for outliers and handle them if needed.

# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Z-scores
# We're going to add a column to the dataset for each numeric feature that contains a standardized z-score. We'll leave the original columns unaltered so the original data are still accessible. 

# In[28]:


medical_raw['Zscore_Population'] = stats.zscore(medical_raw['Population'])
medical_raw['Zscore_Children'] = stats.zscore(medical_raw['Children'])
medical_raw['Zscore_Age'] = stats.zscore(medical_raw['Age'])
medical_raw['Zscore_Income'] = stats.zscore(medical_raw['Income'])
medical_raw['Zscore_Doc_visits'] = stats.zscore(medical_raw['Doc_visits'])
medical_raw['Zscore_Full_meals_eaten'] = stats.zscore(medical_raw['Full_meals_eaten'])
medical_raw['Zscore_Initial_days'] = stats.zscore(medical_raw['Initial_days'])
medical_raw['Zscore_Total_charge'] = stats.zscore(medical_raw['Total_charge'])
medical_raw['Zscore_Additional_charges'] = stats.zscore(medical_raw['Additional_charges'])

medical_raw['Zscore_Item1'] = stats.zscore(medical_raw['Item1'])
medical_raw['Zscore_Item2'] = stats.zscore(medical_raw['Item2'])
medical_raw['Zscore_Item3'] = stats.zscore(medical_raw['Item3'])
medical_raw['Zscore_Item4'] = stats.zscore(medical_raw['Item4'])
medical_raw['Zscore_Item5'] = stats.zscore(medical_raw['Item5'])
medical_raw['Zscore_Item6'] = stats.zscore(medical_raw['Item6'])
medical_raw['Zscore_Item7'] = stats.zscore(medical_raw['Item7'])
medical_raw['Zscore_Item8'] = stats.zscore(medical_raw['Item8'])


medical_dropped = medical_raw


# In[29]:


drop = medical_dropped.query('(Zscore_Population > 3) or (Zscore_Population < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[30]:


drop = medical_dropped.query('(Zscore_Children > 3) or (Zscore_Children < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[31]:


drop = medical_dropped.query('(Zscore_Age > 3) or (Zscore_Age < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[32]:


drop = medical_dropped.query('(Zscore_Income > 3) or (Zscore_Income < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[33]:


drop = medical_dropped.query('(Zscore_Doc_visits > 3) or (Zscore_Doc_visits < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[34]:


drop = medical_dropped.query('(Zscore_Full_meals_eaten > 3) or (Zscore_Full_meals_eaten < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[35]:


drop = medical_dropped.query('(Zscore_Initial_days > 3) or (Zscore_Initial_days < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[36]:


drop = medical_dropped.query('(Zscore_Total_charge > 3) or (Zscore_Total_charge < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[37]:


drop = medical_dropped.query('(Zscore_Additional_charges > 3) or (Zscore_Additional_charges < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[38]:


drop = medical_dropped.query('(Zscore_Item1 > 3) or (Zscore_Item1 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[39]:


drop = medical_dropped.query('(Zscore_Item2 > 3) or (Zscore_Item2 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[40]:


drop = medical_dropped.query('(Zscore_Item3 > 3) or (Zscore_Item3 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[41]:


drop = medical_dropped.query('(Zscore_Item4 > 3) or (Zscore_Item4 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[42]:


drop = medical_dropped.query('(Zscore_Item5 > 3) or (Zscore_Item5 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[43]:


drop = medical_dropped.query('(Zscore_Item6 > 3) or (Zscore_Item6 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[44]:


drop = medical_dropped.query('(Zscore_Item7> 3) or (Zscore_Item7 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[45]:


drop = medical_dropped.query('(Zscore_Item8 > 3) or (Zscore_Item8 < -3)')
medical_dropped = medical_dropped.drop(drop.index)


# In[46]:


medical_dropped.shape


# In[47]:


medical_dropped.to_csv('data/medical_clean.csv')


# # Principle Component Analysis

# In[48]:


# Extract the continuous variables
X = medical_dropped[['Population', 'Children', 'Age', 
                 'Income', 'Doc_visits', 'Full_meals_eaten', 
                 'Initial_days', 'Total_charge', 'Additional_charges']]


# In[49]:


# normalize the data
norm = (X - X.mean()) / X.std()


# In[50]:


pca = PCA(n_components=X.shape[1])
pca.fit(norm)
medical_pca = pd.DataFrame(pca.transform(norm), columns=['PC1','PC2','PC3',
                                                         'PC4','PC5','PC6',
                                                         'PC7','PC8','PC9'])


# ## Scree Plot

# In[51]:


plt.plot(pca.explained_variance_ratio_)
plt.xlabel('number of components')
plt.ylabel('explained variance')
plt.savefig('plots/pca_scree.png')
#plt.show()


# In[52]:


for pc, var in zip(medical_pca.columns,np.cumsum(pca.explained_variance_ratio_)):
    print(pc,var)


# In[53]:


medical_reduced = medical_pca.iloc[:,0:6]
print(medical_reduced)
medical_reduced.to_csv('data/medical_reduced.csv')


# ## Eigenvalues

# In[54]:


cov_matrix = np.dot(norm.T, norm) / norm.shape[0]
eigenvalues = [np.dot(eigenvector.T, np.dot(cov_matrix, eigenvector)) for eigenvector in pca.components_]


# In[55]:


plt.plot(eigenvalues)
plt.xlabel('number of components')
plt.ylabel('eigenvalue')
plt.plot([0, 9], [1, 1], color='red', linestyle='dashed', linewidth=2)
plt.savefig('plots/pca_eigenvalues.png')
#plt.show()


# In[56]:


i = 1
for e in eigenvalues:
    print("PC" + str(i) + " " + str(e))
    i +=1


# eigenvalue is >1 for components 1-5

# ## Loadings

# In[57]:


loadings = pd.DataFrame(pca.components_.T, 
                        columns=['PC1','PC2','PC3',
                                'PC4','PC5','PC6',
                                'PC7','PC8','PC9'],
                        index=norm.columns)
loadings


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




