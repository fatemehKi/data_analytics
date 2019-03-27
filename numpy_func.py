# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:56:13 2019

@author: mfatemeh
"""

'''
- if we have the numbers mostly we use tnumpy but for heteregenous we use panda
- in numpy we have one dimension like list, 2D like metrix 
- we can have special built in data type in panda as well as panda  
- to create an array 1. we can use np.array([1,2] or np.array(lst))
- to create a 2d array we need to have in 
- myarray2.ndim giving us the number of dimension; however, shape gives us what is the dimenssion
- the dimension needed to be balanced if we do not follow the balance it will change to the one dimension
- arange is similar to the range in the numpy; however, the output is the array and one dimension
'''
import numpy as np
myarray=np.array([1,2,3]) #if we add the [] inside the () it will change to 
print(myarray)
myarray[0]
type(myarray) #ndarray means multi dimensional array
len(myarray) # give the number of elements

#the dimension of array
myarray.shape #gives the number of column and row here we have nothing in the row        


#######################2D
myarray2=np.array([[1,2,3], [4,5,6]]) # 2D first element first row and the second element in seconf row
myarray2
myarray2.itemsize # default size of the array is 4 (32 bits) and can be changed to any number
myarray2=np.array([[1,2,3], [4,5,6]], dtype=np.int64)
myarray2=np.array([[1,2,3], [4,5,6]], dtype=np.int32) # the default
myarray2=np.array([[1,2,3], [4,5,6]], dtype=np.int) # the default

#the dimension of array
myarray2.shape              

# for the slicing indexes stating.. gettinf 2nd row and 3rd column.. first row and then column
myarray2[1,2]

myarray2[1:2] #row number is firsttherefore if we have only one element without ',' it menas only the first
myarray2[1:2, :]

myarray2[1,:] #equivalent 
myarray2[1,] 

myarray2[0:2,:]
myarray2[0:2,]

myarray3=np.array([[1,2,3]]) #because of the extra [] we created a dimension to this however, the 
myarray3.shape  
myarray2.ndim 

print(myarray2)

#############################3D repeating a 2D after a , insidde another [] will give is another dimension
myarray4=np.array([[[1,2,3], [4,5,6]], [[0,0,0], [40,50,60]]]) #2 depth(slice), 2 rows and 3 column and 
print(myarray4)
myarray4.shape #first is depth, 2nd is rows and tht 3rd is the column

myarray4[1,1,2] #to get 60; first is depth(slice), 2nd is rows and tht 3rd is the column inside the row

myarray5=np.array([[[1,2,3], [4,5,6]], [[0,0,0], [40,50,60]], [[15,25,35], [45,55,65]]]) # 3 slice, 2 rows, 3 column and      
myarray5[2,1,2] #to get 65; first is depth(slice), 2nd is rows and tht 3rd is the column inside the row

myarray4[1,0:2,2]       
               
b=np.arange(1,9,2)
b= np.arange(1,9)
b= np.arange(9)
type(b)
b.ndim
