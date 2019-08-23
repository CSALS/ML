# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 06:16:02 2019

@author: Charan
"""

import pandas as pd
import numpy as np
#Pandas is a library that allows you to read datasets (excel,csv files)
#and store the content in what you'd call a dataframe


#SERIES,DATAFRAME -> Learn later
#Series Data Type
#Series object is similar to NumPy Array (built on top of numpy array object)
#Series can have axis labels, meaning it can be indexed by a label, instead of just a number location.

#CREATING A SERIES

#list/numpy array/dictionary can be converted to series


#DATA INPUT AND OUTPUT

df = pd.read_csv('example')

df = pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')