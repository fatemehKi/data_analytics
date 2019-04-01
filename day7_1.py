# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 00:41:24 2018

@author: Tareq
"""
import os
os.chdir(r'C:\Users\tjaber\Desktop\examples')

import numpy as np

myarray= np.array([1,2,3])#1D
myarray.shape
myarray= np.array([[1,2,3]])#2D

myarray.ndim

print(myarray)
myarray[0]
type(myarray)
len(myrray)


myarray= np.array([[1,2,3], [4,5,6]])#2D
print(myarray)
myarray[0:2,1]

myarray= np.array([[1,2,3], [4,5,6]], dtype=np.int64)
myarray= np.array([[1,2,3], [4,5,6]], dtype=np.int32)
myarray= np.array([[1,2,3], [4,5,6]], dtype=np.int)
myarray.itemsize

myarray.shape

myarray= np.array([[[1,2,3], [4,5,6]]])#2D
print(myarray)
myarray= np.array([[[1,2,3], [4,5,6]],[[10,20,30], [40,50,60]],[[15,25,35], [45,55,65]]])#3D

myarray.shape

myarray[1,1,2]



b = np.arange(1, 9, 2)
b = np.arange(1, 9)
b = np.arange(9)
type(b)
b.ndim

#---------------------------------

c = np.linspace(0, 1, 6)
print(c)
type(c)


c = np.linspace(0, 1, 6, endpoint=False)


x=np.ones((3,4))
print(x)
x.shape
x=np.ones(3)
print(x)
x.shape


x=np.ones((3,4), int)
len(x)
x.shape
x.size


np.zeros((2,3,4))

np.empty((3,4))
np.empty((3,4), int)
np.eye(3)
np.full((2,2), 7)

np.random.random([2,3])


a = np.arange(100)
a
a.shape
a.ndim
a = a.reshape((10, 10))
a
a.shape
a.ndim
np.savetxt('data_a.txt', a)

b = np.loadtxt('data_a.txt')
b.shape
b
#**************************************************************
#-------------------------------
#a Python program to print the NumPy version in your system.
print(np.__version__)

#-------------------------------#-------------------------------
#a Python program to convert a list of numeric value into a one-dimensional NumPy array.
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l)
print("One-dimensional numpy array: ",a)
type(a)
type(l)

l.shape
a.shape


b = np.array((1,2,3,4,7,8,9))
b

#-------------------------------
#a Python program to create a null vector of size 10 and update sixth value to 11.

x = np.zeros(10)
print(x)
print("Update sixth value to 11")
x[6] = 11
print(x)

#-------------------------------
#a Python program to reverse an array 
x = np.arange(12, 38)
print("Original array:")
print(x)
print("Reverse array:")
x = x[::-1]
print(x)

#-------------------------------
#a Python program to an array converted to a float type
a = [1, 2, 3, 4]
print("Original array")
print(a)
x = np.asfarray(a)
print("Array converted to a float type:")
print(x)

#-------------------------------
#a Python program to create a 2d array with 1 on the border and 0 inside.
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)
x[2:-2,2:-2] = 0

x[2:-1,2:-1] = 0



#-------------------------------
#a Python program to add a border (filled with 0's) around 
#an existing array.

x = np.ones((3,3))
print("Original array:")
print(x)
print("0 on the border and 1 inside in the array")
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)

help(np.pad)

#-------------------------------
#a Python program to convert a list and tuple into arrays.

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
x=np.asarray(my_tuple)
x=np.array(my_tuple)
x
np.asfarray(x)
print(x)
x.ndim
x.shape
#-------------------------------
#a Python program to append values to the end of an array.

x = [[10, 20, 30], [1,2,3]]
print("Original List:")
print(x)
x = np.append(x, [[40, 50, 60], [70, 80, 90]],axis=1)#axis =0, axis=1
print("After append values to the end of the array:")
print(x)
type(x)
x.shape
x.ndim
#-------------------------------
#a Python program to convert the values of 
#Fahrenheit degrees into Centigrade degrees.
fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:") 
print(5*F/9 - 5*32/9)

#-------------------------------
#a Python program to find the real and imaginary 
#parts of an array of complex numbers
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ",x)
print("Original array:y ",y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)

#-------------------------------
#a Python program to interchange two axes of an array.
x = np.array([[1,2,3]])
print(x)
x.shape
x.ndim
y =  np.swapaxes(x,0,1)
print(y)
y.shape

x=np.array([1,2,3])
print(x)
x.ndim
y =  np.swapaxes(x,0,1)#!!!

x=np.array([[[1,2,3]], [[4,5,6]]])#3d
print(x)
x.shape
y =  np.swapaxes(x,1,2)
print(y)
 y.shape
z =  np.swapaxes(x,0,2)#????
z
#-------------------------------
#a Python program to split an array
x = np.arange(1, 15)
print("Original array:",x)
print("After splitting:")
print(np.split(x, [2, 6]))#replace with a single integer
y=np.split(x, [2, 6])
z=y[0]
y[1]
y[2]
z
#-------------------------------
#a Python program to get the number of nonzero elements in an array.
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array:")
print(x)
print("Number of non zero elements in the above array:")
print(np.count_nonzero(x))

#-------------------------------
#a Python program to make an array immutable (read-only).
x = np.zeros(10)
x.flags.writeable = False
print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
x[0] = 1

#-------------------------------
#a Python program to sum of all the multiples of 3 or 5 below 100.
x = np.arange(1, 100)
x
# find  multiple of 3 or 5
n= x[(x % 3 == 0) | (x % 5 == 0)]
print(n)
# print sum the numbers
print(n.sum())

#-------------------------------
#a Python program to combine a one and a two dimensional array together and display their elements.
x = np.arange(4)
print("One dimensional array:")
print(x)
y = np.arange(8).reshape(2,4)
print("Two dimensional array:")
print(y)
for a, b in np.nditer([x,y]):#nditer: multi-dimensional iterator object to iterate over arrays
    print("%d:%d" % (a,b),)

#-------------------------------
#a Python program to test whether each element of a 1-D array is also present in a second array.
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [0, 40]
print("Array2: ",array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))#intersect1d, union1d 

#-------------------------------
#a Python program to find the set exclusive-or of two arrays.
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values that are in only one (not both) of the input arrays:")
print(np.setxor1d(array1, array2))#setdiff1d

#-------------------------------
#a Python program to get the unique elements of an array.
x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))
x = np.array([[1, 1], [2, 3]])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))

#-------------------------------
# a Python program to construct an array by repeating.
a = [1, 2, 3, 4]
print("Original array")
print(a)
print("Repeating 2 times")
x = np.tile(a, 2)
print(x)
print("Repeating 3 times")
x = np.tile(a, 3)
print(x)
#-------------------------------
#Max and Min
x = np.array([1, 2, 3, 4, 5, 6])
print("Original array: ",x)
print("Maximum Values: ",np.argmax(x))#index
print("Minimum Values: ",np.argmin(x))#index

x[np.argmax(x)]
#--------------------------------















