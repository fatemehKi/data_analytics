# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:33:51 2019

@author: mfatemeh
"""

'''
- copy by reference vs copy by value
 in the copy by value the change in the copy by valueis not changing the original but 
- if we have copy by reference we don't vhange the original
- in python 3 we can not get the value of the object without using the list
- range always stops at the end of n-1
-------------------------------TUPLE
- tuples can be misture type (heterogenous) and they are immutable (can not be changes) 
- we use the bracket to define a tuple or using tuple() functions
- we can have tuple inside the tuple
- tuple vs list: tuple is immutable but list is mutable and also tuple is using () and list is using []
    list_num = [1,2,3,4]
    tup_num = (1,2,3,4)
- in order to get into the nested tuple we need to use [i][j] where i showing the index for the main tuple and 
j is related to the nested tuple
- how do we now it is tuple.. from the bracet
- creating a tuple using one element a, you can use X(a,)
- we can even create a tuple without even paarntheses
- multiplicatio  can creates 
- integer and tuple can not be in the same operator
- in the dictionary we use the key to get the values
- we can use the syntax of tuple to assign multiple values
- although the tuples are immutable, the nested list inside the tuple can be mutable
-------aggregate functions
- the aggregate functions are not applicable for heteregenous but applicable for the alphanbet alone (or numeric alone)
- applying a tuple function to the string will result a tuple with all individual chars of that spring
------------ LIST
- we do fefine the list with [] amd we add the values using append
- the for loop in the python ineeds to have : at the end and the statments inside the for loops are as long
as the indenting exists and the indent needed to be exactly the same in all lines.
- the print function in python will go to the next line automatically
'''

mylist = range(1,9)
mylist #nothing is shown in python 3
mylist=list(range(1,9))
mylist #showing the value


mylist2=mylist #coppied by reference
mylist2
mylist3=mylist[:] #coppied by value
mylist3

mylist2[3]=100;
mylist2
mylist

mylist3[4]=150
mylist3  
mylist

'''------------------- TUPLES--------'''
T=(2, 'abc', 4.56, (200,100), 22.82) #defining a tuple inside a tuple.. defining the tuple using the data creation
print(type(T), T)
print(type(tuple(range(1,10))), tuple(range(1,10)))#creating tuple using the tuple() function
T[0]
T[2]
T[3]
T[3][1] 
T[0]=99 # is an error because tuples are immutable

     
T2=(2, 'abc', 4.56, [2,1], 22.82)
print(type(T2), T2) # it is still tuple


(1,)*5 # the size of tuple increaed.. repeating the values 
(1,2)*5

(1,)+5 #error
(1) + 5 #addition of two integer
(1,2) +(5,) # concatenation of two tuple

t5=(1,2,3,3,5,5,5)
t5.count(5) #how many 5 is in the tuple
t5.index(3) # you get the location of value 3 in the tuple

#the below are not tuples but multiple assigning.. we are using the syntax of tuple we for multi assigning
(x,y,z)=('a','b',4)
x
z
# it is similar to the below because tuples can be used without the ()
x,y,z = 'a', 'b', 4
x

(x,y,z)=range(3)
x

tuple(range(1,4)) #output is (1, 2, 3)
tuple(range(4)) #(0, 1, 2, 3)

data=(1,2,3) #creating tuple
x, y, z =data #unpacking a tuple
x
z

#swapping the value
(x,y)=(y,x)
x
y

#finding the length of a tuple
t=(1,2)
len(t)

#slicing in the tuple(extracting a segment)
t=tuple(range(1,6))
t
t[2:]

#------- LIST and TUPLE
lst=list(range(1,4))
lst
#or
lst2=[1,2,3]
lst2

t7 = (1,5,'ttrr', ['a','b'], 5.7)
t7[0]
t7[2]
t7[3]=99 #error because tuple is immutable
t7[3][1] #toaccess the nested list inside a tuple\
t7[3][1]=6 # the nested list is mutable therefore we can change without error
t7

#some Aggregate functions max, min, 
t8=range(10) #returns a sequence
max(t8)
min(t8)

max(t7) #error 

t9=('z', 'g', 'google')
max(t9)
min(t9)

t10=tuple(range(10))
t10
5 in t10 #the answer is true
5 not in t10 # the answer is false
100 in t8

z in t9

5 in t8 #even if it is not tuple it still works the same

('z' in t9) and (100 in t8)
('z' in t9) and ('k' not in t8)

s='python2019'
s[0] #string is iterable
tuple(s) 

s2= 10
tuple(s2)#error because int is not iterable.. strings unlike integer can be found using the index like S[0]
list(s2)#error

'''-----------list------'''
mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist

print (mylist[0])
print (mylist[1])
print (mylist[2])
print (mylist[10]) #error out of the range

      
#prints out 1,2,3
for x in mylist: #the end of the loop is shown by the indenting, x can be any variables
  print(x*2)
  print(mylist)






