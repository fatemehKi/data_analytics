
"""
Created on Mon Apr  1 10:30:24 2019

@author: mfatemeh
"""

'''
- if the datatypes are different in array all willl change to the powerful one which can be string
- there is a way to change the type of the data 
- 'b' is special character for string in np arrays
- the default type out of loadtxt is float however, we can xhNGW IT LIKE BELOW
- we calling aggregated function because they take a list of many values and return a number
'''

import numpy as np

x=np.array([1, 'a', 2]) # the data type changes to string

from io import StringIO

#####data type structure
x=np.array([(1,2., 'Hello'), (2,3., 'world')],
          dtype=[('foo', 'i4'), ('bar', 'f4'), ('baz','S10')])
x[0]
x[1]
y=x['foo']
y
y=2*y
y
x
x[1]=(-1,-1,1000) #data type conversion happens if we didin't pass the proper datatype

 ######
s=StringIO('1,1.3,abcde')
data=np.genfromtxt(s, dtype=[('myint', 'i8'), ('myfloat', 'f8'), ('mystring', 'S5')], delimiter=',')

s = StringIO(u"1,1.3,abcde")
data = np.genfromtxt(s, dtype=[('myint','i8'),('myfloat','f8'), ('mystring','S5')], delimiter=",")
s.tell()
s.seek(0)


dataset = np.genfromtxt(s, delimiter=',', dtype='i8,f8,str')[1:]

                        
import os
os.getcwd()
os.chdir(r'C:\Users\mfatemeh\Desktop\python')
x=np.loadtxt('Salary.txt', dtype='S10') # the return type of loadtxt is array, loadtxt expecting float unless we change the data type to string
#the default delimiter in loadtxt is tab if we are reading csv we need to show the delimiter as ','
type(x) # we can deal with it like a metrix and everything changes to the string with the character b
x.shape



x[1,9]#error:out of bounds
x[0:2]

y=x[1:4, 1:5]
y.shape
z=np.transpose(y)
z.shape
s=y.T # T is same as transpose
s.shape

y.reshape(4,4) # error, it will not add element to fit however, the resize does
np.resize(y,(5,5)) # it does change the size and keep looping on the lements from the beginbing

#using the unpacking feature in the tuple and assigning eaxh to the 
x1,x2,x3,x4,x5,x6=np.loadtxt('Salary.txt', skiprows=0, unpack=True, dtype ='S')
x1

np.save('ttt', x1) # the output is the binary numpy function which is powerful and can not be changed
x1.size 
x1.nbytes

np.savez('salary_new', x1,x2,x3,x4,x5,x6 ) # the saved file is npyz 
loaded_salary=np.load('salary_new.npz')
type(loaded_salary) # it is array of files, arrays of arrays

loaded_salary['arr_0'] # we get the first column
loaded_salary['arr_1']
loaded_salary[0]


c = StringIO("1,0,2\n3,0,4")
x, y= np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True) #usecol is used to select specific column, unpack=true because we are passinf x, y seperately

x, y, z = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True) #error becuase the number of the variables are more than we are defining 

                    
x, y, z = np.loadtxt(c, delimiter=',',  unpack=True)
                 
#we can change the meanunf of the string by changing 

x, y = np.loadtxt(c, delimiter='\n', unpack=True, dtype='S')

##### if we have multiple condirion

def select1(x):
    return(x<9 and x>3) #error, we can not return multiple boolean statment in return

def select(x):
    return x<9 and x>3

a=np.array([1,2,5])
select(a)

np.vectorize(select)(a) # we passed two boolean statment inside the function

####slicing
x=np.array(range(1,25))
x=x.reshape(6,4)
y=x[(3,4,3,4),(0,0,2,2)] #using this method of slicing we get the element row in the first tuple and column in the second 
y

#----------------------------
#Ravel and Flatten 
#raval will destroy the dimension of the array and turn it to the one dimension 
#raval just will change the view of array but it does get passed by reference; therefore will be changes
x=np.array(range(1,25))
x=x.reshape(6,4)
y=x.ravel()#y view of x
y
x[1,1]=100

# flatten will create a new copy of the 
x=np.array(range(1,25))
x=x.reshape(6,4)
z=x.flatten()
z
x
x[1,1]=100
x
z

#-----------------------------
x = np.array([1, 2, 4, 7, 0])
np.diff(x)# x[i]=x[i+1]-x[i]
np.diff(x, n=2)#n: number of times that we are applying the dff

#### 
coffee = np.loadtxt("coffee_info.csv", delimiter=",", dtype ="S10")#
type(coffee)

coffee_1 = np.loadtxt("coffee_info.csv", delimiter=",", usecols=(0,1,2), dtype ="S10")#
coffee.shape
coffee_1.shape

x=np.random.rand(3,3)#uniform random 

x=np.random.randn(3,3)#normal

np.random.randint(1,8,size=6)

np.random.randint(1,8,size =(2,3))

np.random.randint(5,size=(3,3))

np.random.sample(size=10)#Float in (0,1)


np.random.sample(size=10)#Float in (0,1)
np.random.random(size=10)#Float in (0,1)
np.random.ranf(size=10)#Float in (0,1)
np.random.random_sample(size=10)#Float in (0,1)

np.random.seed(123456)

np.random.seed(10)
np.random.rand(10)##########

#mer
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack((a,b))# #2D because we have two []
np.hstack((a,b)) #1D because we have two []
np.concatenate((a,b),axis=0)#axis=1??
np.concatenate((a,b),axis=1) # error because we don't have second axis, a,b shoulb 2D then we have acess

a = np.array([[1, 2, 3]]) #2D
b = np.array([[4, 5, 6]]) #2D
np.concatenate((a,b),axis=0)#axis=1
np.concatenate((a,b),axis=1)

np.column_stack((a,b)) #the column stack is different in 1D in 2D when we apply clumn stack or row stack
#because we don't have the second D (column) in the 1D
np.row_stack((a,b)) # similar to the 1D, 2D has two dimension

a.itemset(2,100) #in place change.. meaning it changes an existing location
b.itemset(2,100)




