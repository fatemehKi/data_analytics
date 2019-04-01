# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:49:10 2018

@author: Tareq
"""

import os
os.chdir(r'C:\Users\tjaber\Desktop\examples')

import numpy as np

#----------------------------
#Loading text
from io import StringIO


x=np.array([1,"b",2])
x
#Numpy provides powerful capabilities to create arrays of structured datatype.
x = np.array([(1,2.,'Hello'), (2,3.,"World")],
   dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])
x[0]
y = x['foo']
y
y= 2*y
y
x
x[1] = (-1,-1.,"Master")
x
#----------------------------
s = StringIO("1,1.3,abcde")
data = np.genfromtxt(s, dtype=[('myint','i8'),('myfloat','f8'),
('mystring','S5')], delimiter=",")#Default output data type: float
data
s.seek(0)
#----------------------------
x=np.loadtxt('Salary.txt', dtype= 'S10')#Default output data type: float
#dtype={'names': ('gender', 'age', 'weight'), 'formats': ('S1', 'i4', 'f4')}
x[9]#single value: row
x[1,9]#error: out of bounds
x[0:2]#rows 0 and 1
x[0:2,1]#2 items
x[1,2]#one item

y=x[1:4,1:5]#Slicing
y.shape
z=np.transpose(y)
z.shape
s=y.T#Transpose
s.shape

np.resize(y,(5,5))#change the size
y.reshape(4,3)#No change! 

x1,x2,x3,x4,x5,x6=np.loadtxt('Salary.txt', skiprows=0, unpack=True, dtype ='S')
np.save("ttt", x1)#Saves only a single array: binary file
x1.size
x1.nbytes
x1.itemsize
np.savez("salary_new", x1,x2,x3,x4,x5,x6)#x1=x1, x2=x2.....
#NPZ is a file format by numpy that provides storage of array data using gzip compression.
loaded_salary= np.load("salary_new.npz")
loaded_salary.files
loaded_salary['arr_0']
#----------------------------
 c = StringIO("1,0,2\n3,0,4")
x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)

x, y, z = np.loadtxt(c, delimiter=',', unpack=True)

x, y = np.loadtxt(c, delimiter='\n', unpack=True, dtype='S')#byte data type output, x.decode('utf8') converts to string. 
#----------------------------
def select(x):
    return x<9 and x>3

a=np.array([1,2,5])
select(a)#Error
np.vectorize(select)(a)
#----------------------------
#Slicing
x=np.array(range(1,25))
x=x.reshape(6,4)
y=x[(3,4,3,4),(0,0,2,2)]
y
#----------------------------
#Ravel and Flatten
x=np.array(range(1,25))
x=x.reshape(6,4)
y=x.ravel()#y view of x
y
x[1,1]=100
x
y

z=x.flatten()#z is a new array
z
x
x[1,1]=100
x
z
#-----------------------------
x = np.array([1, 2, 4, 7, 0])
np.diff(x)
np.diff(x, n=2)#n: number of times
#-----------------------------














