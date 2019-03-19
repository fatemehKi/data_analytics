# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:54:39 2019

@author: mfatemeh
"""

'''
- the missing value in the python array y can be found using np.isnan(y) and the output is a boolean array
that the size equals to the y array
- in the numpy package "NaN" represents missing and in the panda the missing values are shown as "Na"
- panda is better to handle missing data.. numpy is more on math and statistics and panda is more the data anlysis and visualisation
- range is a methos in python that we can use to get the dvalues from first to n-1
- :: shows the step of 2
- python is case sensitive
- any indexing operation needed to be the in []
- shapes giving the dimension
- A.head(10) showing the first 10 rows
- we can specify multiplechars showing the missing
X=pd.read_csv("c:\\data.csv", na_values=[' ', ','] )
- in pandas Y=X.isnull() used to have a boolean results showing where is missing; the agains result Z=X.notnull()
and in the numpy we have isnan
- each colum is a series and multiple 
'''

import numpy as np #np is the alternative name for the numpy
y=np.array([1, 0, np.NaN, 0, np.NaN, 0, 9]) #the numbers are dealt as the numbers in python
print(y)

#counting how many missing value is in the array
z=np.isnan(y)
print(z)
z.sum() #z is the object
#finding the percentage of missing values in my array
np.mean(z)

#another way of handling missing data
import pandas as pd
X=pd.Series(range(11,18), index=range(1,8)) # the defult index stary from 0 but I want to get it from 1 till 8-1
X
Y=X[::2] #not all elemnts but every other elements
Y

A=X.reindex([2,1,12,3], fill_value=0.0) #meaning to replace the nan with the 0
B=X.reindex([2,1,12,3], fill_value=0) #integer type
C=X.reindex([2,1,12,3])
A
B
C

X.shape #series are one dimension 
X.size

C.size #even the nan is counted



