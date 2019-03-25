# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:14:45 2019

@author: Kian
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Fatemeh
This is a temporary script file.
"""
x=10
x
print(x)

'''
- python is case sensitive but not sensitive to the space
- to get the integer value we put double/ (meaning //)
- naming vars: can not start with the number but number can be other places in the name
- packages are the series of the functions, data sets, objects.. that we can import and call them 
- the histograms are used for the frequecy among the unique value in the same column
- scatters are used for the correlation of two variabels
- in the sequence type(tuple,list) the order is important but not in non-sequence type(dictionary, set)
- type(name_of_theobject) is used to identify the type of variable(object)
- applying the type function to the set (collection type) we get different
- none used like a value in python but can not be used with operation.. none can be used for the missing value handling
- collection type: to create tuple we use () for the list we use [] and we use {} for dictionary and we use the following 
script a_set =set(a_tuple) for the set
- tuple is immutable order sequence, can not be updated, but list is mutable ordered sequence
- str function turns a numeric to the string
- in python we are indexing from '0' (unlike R which is from '1'); therefor, the character are stored from 0 to len(s)-1
- s.find('word' 0, 50): finding the location of the specific word in the string.. starting from 0 and we need to enter the start and end index as well
- s.capitalize(): capitalizing the first character in the string
- s.count('chr'): giving the number of character in the string s
- 3+4                #addition operator
  'fatemeh'+' kiaie' #concatination
  'abc' + 10         #giving error
  'abc' + str(10)    #we need to convert the number to the string
- s.lower() returns the lower case of all chars in the string s
- s.upper() returns the upper case of the all chars in the string
- s.replace('right', 'correct') replace the first char with the second    
- s.split(',') spliting based on the character  ','

- getting the slice of a string s[2:7]...s[a:b].. geting from location 2 to 6
- if we put negative for the number s[a:-b].. then we get the same ch
z[0:4]#it does exclude tnumber 4 (n-1)
z[0:-3]# we will exclude this slice (in positive number) sso we count from right 0, 1,2 and then we will have the rest of the string
- to have a word qutoted inside another quotation, we need them to be in the different quotation type (one single, the other double)
or we cam ise the \ to get the corect 
- "\n": new line "\t": new tab "\r": escape or over writting to the previous char 
- using r we will say please treat the coming text like a raw data
- os.getcwd()#getting directory
- from "package_name" import "subpackage1", "subpackage"
- for the datetime package we can use : https://www.journaldev.com/23365/python-string-to-datetime-strptime
'''

5/2
10/3 #float
10//3 #integer

2V=5 #2v is not valid
v2=5

x= 17
type(x)
z=1.5
type(z)
y='123'
type(y)

print(type(y))

5%2
4%2

x=10
x=x+5
x
x+=5
x

y=2
y**=3
y

a =True #case sensitive
b =False
a==True
a==1
b==0 #0 amd 1 or the alternatives for true and false


x=1
x==10#logical operation

X=8
Y=3

A=(X>5)
B=(Y>5)


A&B 
A and B

A|B
A or B

A^B 
A != B #bitwise != equal to the ^ but if we have a number that can not be useed for the XOR

#not equal != amf not(A&B)


c=str(10)
c
type(c)

s ='abcd'
len(s)
s[0]
s[1]
s[3]
s[4] #error because we don't have location 4

x='this is a right way, right'
x.find('right', 0, 50) 
x.find('right', 11, 50)
x.capitalize()
x.count('right')
'the length is '+str(len(x)) 
x.lower() 
x.upper()        
x.replace('right', 'correct')
x.replace('right', 'correct', 1)
x.split() #split based on the space
x.split(',') #split based on the comma
q='|'.join(x) #seperating each char with the pipe (|)

#string slicing application
z='tarek' + ' kkk'
z
z[0:4]#it does exclude tnumber 4 (n-1)
z[0:-3]# we will exclude this slice (in positive number) sso we count from right 0, 1,2 and remove those and then we will have the rest of the string

A="This is called 'Milk'" # to use quotation inside quotation
A

a='AAA'
b='BBBBB'
c='CCC'

print(a+ '\n' +b+ '\n' +c)       

print(a+ '\t' +b+ '\t' +c)           

print(a+ '\r' +b+ '\r' +c)  
print(a+ '\n' +b+ '\r' +c)      

print ('abc\tdef') # \t is the tab between the chars
print (r'abc\tdef') # r is used to say use the raw data

import os
os.getcwd()#getting directory         
os.chdir('C:\Users\mfatemeh\Desktop\in share\python')#error because of the \ in python is \\
#two ways: using 'r' after r it is treated as raw character
os.chdir('C:\\Users\\mfatemeh\\Desktop\\in share\\python')
#or
os.chdir(r'C:\Users\mfatemeh\Desktop\in share\python')

#Importing the packages and subpackages
from datetime import datetime, date, time, timedelta
my_var=datetime(2013,5,17,16,21,18)
print(my_var)
#changing the style of the output
my_var2=datetime.strptime("20130517@162118","%Y%m%d@%H%M%S")
print(my_var2)

#converting to string
my_var3=my_var2.strftime("%m/%d/%Y %H:%M")
print(my_var3)
