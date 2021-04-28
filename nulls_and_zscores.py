import numpy as np
import pandas as pd
from pandas import DataFrame
import scipy.stats as stats
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

# import
medical_raw = pd.read_csv('../data/medical_raw_data.csv')


medical_raw.rename(columns = {'TotalCharge': 'Total_charge'}, inplace=True)

# fill nulls
medical_raw['Children'].fillna(method='bfill', inplace=True)
medical_raw['Age'].fillna(round(medical_raw['Age'].mean()), inplace=True)
medical_raw['Income'].fillna(medical_raw['Income'].mean(), inplace=True)
medical_raw['Soft_drink'].fillna(medical_raw['Soft_drink'].mode()[0], inplace=True)
medical_raw['Overweight'].fillna(medical_raw['Overweight'].mode()[0], inplace=True)
medical_raw['Anxiety'].fillna(medical_raw['Anxiety'].mode()[0], inplace=True)
medical_raw['Initial_days'].fillna(medical_raw['Initial_days'].mean(), inplace=True)

# zscores
medical_raw['Zscore_Population'] = stats.zscore(medical_raw['Population'])
medical_raw['Zscore_Children'] = stats.zscore(medical_raw['Children'])
medical_raw['Zscore_Age'] = stats.zscore(medical_raw['Age'])
medical_raw['Zscore_Income'] = stats.zscore(medical_raw['Income'])
medical_raw['Zscore_Doc_visits'] = stats.zscore(medical_raw['Doc_visits'])
medical_raw['Zscore_Full_meals_eaten'] = stats.zscore(medical_raw['Full_meals_eaten'])
medical_raw['Zscore_Initial_days'] = stats.zscore(medical_raw['Initial_days'])
medical_raw['Zscore_Total_charge'] = stats.zscore(medical_raw['Total_charge'])
medical_raw['Zscore_Additional_charges'] = stats.zscore(medical_raw['Additional_charges'])
