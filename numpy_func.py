# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:56:13 2019

@author: mfatemeh
"""

'''
- if we have the numbers mostly we use numpy but for heteregenous we use panda
- if we create a numpy array then by creating the object and then . will give us all attribure that exists for the nump
- in numpy we have one dimension like list, 2D like metrix 
- we can have special built in data type in panda as well as panda  
- to create an array 1. we can use np.array([1,2] or np.array(lst))
- to create a 2d array we need to have in 
- myarray2.ndim giving us the number of dimension; however, shape gives us what is the dimenssion
- len in 2D, 3D array will gives only rows to get the number of elements we need to use size
- the dimension needed to be balanced if we do not follow the balance it will change to the one dimension
- arange is similar to the range in the numpy; however, the output is the array and one dimension
- when we asked for the type the nd means the multi-dimension 
- in linspace we have start point and the end point and the number of steps.. the space is equal
- the return of linspace is array and the application is sampling and graphing
- if we put np.linspace(0, 1, 6, endpoint=False), meaning the endpoint =False, we can get the same value
- np.ones((3,4)) showing the matrix with the value of one and the dimension is pased by a tuple; the output is float by default
- np.zero((3,4,5)) showing the 3d with the value of zero with the dimension is pased by a tuple
- there is no data inside the empty array and it gives a random number and the main purpose of having is to fill it after
to read from webserver
- np.eye(one dimension) is the diagonal matrix with one in the diagonal
- np.full((), value), we can have a multi dimension () array that all elements are value
- to generate random value we use .random method.. the result is unf=iform distribution
- we can change the dimension by reshape and total size of new array must be unchanged
- savetxt() is a np function and 
- np.__version__ gives the numpy version
- we can pass a list/tuple and create an array and the we have access to all methods of np array
- shape doesn't work for the list and it works on array
- to reevrse an array we can have a[::-1]
- to connvert from integer to float np.asfarray(a)
- the last row and column in array can be shown by -1 in index
- using np.asarray converting tuple and list to array without changing int to float (which was
coming in the above method of array creation) moreover asarray gives the nested tuple or list a dimension
- list vs  arary is ',' in the list not in array
- x=np.append(x, list)
- split an array in specific location
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
len(myarray2) # len in 2D array will gives only row

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
               
b= np.arange(1,9,2)
b= np.arange(1,9)
b= np.arange(9)
type(b)
b.ndim

c=np.linspace(0,1,6)
print(c)

c2=np.linspace(0,1,5) #(start, endpomt and number of the steps).. (end -start)/(n-1)
print(c2)

c3=np.linspace(0, 1, 6, endpoint=False) #meaning that we are not going to get to the 1

c4=np.linspace(0,1,7) # it equals to the above; however, we 
print(c4)

x=np.ones((3,4)) #(3,4) is the tuple showing the dimension
x
type(x)
x.shape
x.size

x2=np.ones(3) #(3,4) is the tuple showing the dimension
x2
x2.ndim
x2.shape

y=np.zeros((2,3,4)) #2 slice and 3 rows and 4 column
y

z=np.empty((3,4))# it is a random number can be 0 or 1 or..
z
np.empty((3,4), int) #random integer

np.eye(3)

np.full((2,2), 7)
np.full((3,4), 5)

np.random.random([2,3])

a=np.arange(100)
a
a.shape
a.ndim

b=a.reshape(10,10)
b.shape
b.ndim

b2=a.reshape(10,5) #error: the total size of new array must be unchanged

import os
os.getcwd()
os.chdir(r'C:\Users\mfatemeh\Desktop\python')
np.savetxt('data_b.txt',b) #we are saving the data in b inside the file name data

c=np.loadtxt('data_b.txt') # the data changed to float however, it was integer
c.shape 

print(np.__version__)

#######
l=[12.23, 13.32, 100, 36.32] #can be tuple as well
print('Original List:', l)

a=np.array(l)
print('one_dimension numpy array:',a)

type(a)
type(l)

a.shape #
l.shape #error

#since arary are mutable we can assign a number to any element
x=np.zeros(10)
print(x)
x[6]=11
print(x)

#######to revese an array
x=np.arange(12,38)
print('Original array:')
print(x)
print('reverse array:')
x=x[::-1] # if we had a positive number it was hopping but here we hop every -1 and starting from right
print(x)

####### to converting to the float
a=[1, 2,3,4]
print('Original array')
print(a)
x=np.asfarray(a)
print('Array converted to a float type:')
print(x)

######
x=np.ones((5,5))

x[1:-1,1:-1]=0 #using this method we are keeping not changing---to understand in my way we can make the intersection
print(x)
x[2:-2,2:-2]=0
 
x[1:3,1:3]=0

#######padding.. we add what we want to the existing array
x=np.ones((3,3))
print("Original array: ")
print(x)
print("0 on the border and 1 inside in the array")
x=np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)

### to get the help we can use the comment below otr ctrl+I
help(np.pad)

##########converting tuple and list to array without changing int to float (which was coming in the above method of array creation)
# if we pass a nested tuple or nested list it will automaticly gives two dimension
my_list=[1,2,3,4,5,6,7,8]
print('list to array: ')
print(np.asarray(my_list))
my_tuple=([8,4,6], [1,2,3])

my_tuple2=([80,4,6], [1,2])
print("Tuple to array: ")
x=np.asarray(my_tuple2)
x.ndim
x.shape

########### we are appending the nested list to a list(nested list) we get array and the resultung array is one dimension array, having all the 
##all elemnets in one row
x=[[10,20,30], [1,2,3]]
type(x)
x
print(x)
x=np.append(x,[[40,50,60], [70,80,90]])
type(x)
x
print(x)
x.shape
x.ndim

x2=([10,20,30], [1,2,3])
type(x2)
x2
print(x2)
x3=np.append(x2,((40,50,60), (70,80,90)))
type(x3)
x3
print(x3)
x.shape
x.ndim

############if we want to get them in the row and column 
x=[[10,20,30], [1,2,3]]
type(x)
x
print(x)
x=np.append(x,[[40,50,60], [70,80,90]], axis=0)#added row wise
type(x)
x
print(x)
x.shape
x.ndim

x=np.append(x,[[40,50,60], [70,80,90]], axis=1)#added column wise meaning we add those column to the previous columns
print(x)

#########
fvalues=[0,12, 45.21, 34, 99.91]
F=np.array(fvalues)
print('Values in Farenheit', F) # we could put F in the next line of the code #print(F)
print ('values in C', (5*F/9-5*32/9)) #we could put calculation in the next line of the code #print((5*F/9-5*32/9)

###### imaginary
x=np.sqrt([1+0j])
y=np.sqrt([0+1j])

print('the original x', x)
print('the original y', y)
print(x.real)
print(y.real)

print(x.imag)
print(y.imag)

######to reshaping based on the exising array
x=np.array([[1,2,3]]) # the two dimentional array one row and 3 column
print(x)
x.shape
x.ndim

y= np.swapaxes(x,0,1) # the sequece coming from the shape() and 1 showing the dimension of the array if we had 2D the first is row and the second is column
print(y)

x=np.array([1,2,3]) # the one dimentional array
print(x)
x.shape
x.ndim

y= np.swapaxes(x,0,1) # error because it does have only one dimension
print(y)

x=np.array([[[1,2,3]],[[4,5,6]]]) #3D
print(x)
x.shape
y=np.swapaxes(x,1,2)
print(y)
y.shape

z=np.swapaxes(x,0,2)
print(z)

####### spliting an araray on the specified index
x=np.arange(1,15)
y=np.split(x, [2,6]) # 
print(y)
type(y) # it is a list of array
z=y[0]
z[0]
c=y[0][1]
