#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:56:34 2021

@author: curtishammons
"""

import numpy as np
import pandas as pd

medical_raw = pd.read_csv('medical_raw_data.csv')
medical_raw.info()

medical_raw.isnull().any()

# replace nulls
medical_raw['Children'].fillna(method='bfill', inplace=True)
medical_raw['Age'].fillna(method='bfill', inplace=True)
medical_raw['Income'].fillna(medical_raw['Income'].mean(), inplace=True)
medical_raw['Soft_drink'].fillna(medical_raw['Soft_drink'].mode(), inplace=True)
medical_raw['Overweight'].fillna(medical_raw['Overweight'].mode(), inplace=True)
