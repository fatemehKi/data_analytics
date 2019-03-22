# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:32:39 2019

@author: mfatemeh
"""

a=[1,2, 2,3,4,5]
b=[2,3,4,6,7]
c=[]
d=[]
for i in a:
    if (i in b) and (i not in c):
            c.append(i)
            #print(c)
for f in a:
      if f not in c:
            d.append(f)


print(c)
print(d)
