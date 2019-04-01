# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:05:49 2018

@author: Tareq
"""

import os
os.chdir(r'C:\Users\tjaber\Desktop\examples')

import numpy as np

#--------------------------
x=np.random.rand(3,3)#uniform

x=np.random.randn(3,3)#normal

np.random.randint(1,8,size =6)
np.random.randint(1,8,size =(2,3))
np.random.randint(5,size=(3,3))

np.random.sample(size=10)#Float in (0,1)
np.random.random(size=10)#Float in (0,1)
np.random.ranf(size=10)#Float in (0,1)
np.random.random_sample(size=10)#Float in (0,1)
#---------------------------
np.random.seed(123456)#With the seed reset (every time), the same set of numbers will appear every time.
dist=np.random.normal(size=10000)

dist.mean()
dist.std()
"{1} {0}".format(dist.mean(), dist.std())# String output, 0,1 for output order.
dist

np.random.seed(4)
np.random.rand(4)
#-------------------------
#Coffee database
coffee = np.loadtxt("coffee_info.csv", delimiter=",", dtype ="S10")#
type(coffee)
coffee_1 = np.loadtxt("coffee_info.csv", delimiter=",", usecols=(0,1,2), dtype ="S10")#

coffee.shape
coffee_1.shape

#------------------------

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
np.vstack((a,b))#hstack
np.concatenate((a,b),axis=0)#axis=1??

a = np.array([[1, 2, 3]])
b = np.array([[2, 3, 4]])
np.concatenate((a,b),axis=0)#axis=1


np.column_stack((a,b))
np.row_stack((a,b))

a.itemset(2,100)



























