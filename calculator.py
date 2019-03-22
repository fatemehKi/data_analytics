# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:32:57 2019

@author: mfatemeh
"""

'''
- input is a built in function and gets the value from console and the value is saved as the string

'''

a=input('Type in something:')
#this line prints what a is now worth
print(a)

#the input value is by default an string therefore we have to change it to the integer using int function
a= input('enter the first number:')
b= input('enter the second number:')
print(int(a)*int(b))

print(a+b)

#####simulating a caluculator
def addi(x,y):
    return(int(x)+int(y))

def subs(x,y):
    return(int(x)-int(y))

def mult(x,y):
    return(int(x)*int(y))

def divi(x,y):
    return(int(x)/int(y))

a=10

while a != 5:
    a= input('please select your operator: 1. addition    2. substraction    3. multiplication    4. division   5. Exit :  ')
    if int(a)==1:
        b=input('please enter your first number: ')
        c=input('please enter your second number: ')
        d= addi(b,c)
        print(d)
        
    if int(a)==2:
        b=input('please enter your first number: ')
        c=input('please enter your second number: ')
        d= subs(b,c)
        print(d)
        
    if int(a)==3:
        b=input('please enter your first number: ')
        c=input('please enter your second number: ')
        d=mult(b,c)
        print(d)
        
    if int(a)==4:
        b=input('please enter your first number: ')
        c=input('please enter your second number: ')
        d=divi(b,c)
        print(d)

    if int(a)==5:
        break
    
print ('done')

####second solution
while True:
    option=input('please select your operator: 1. addition    2. substraction    3. multiplication    4. division   5. Exit :  ')
    if int(option)==5:
        break #before the start we can get out of the loop
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    if int(option)==1:
        print(int(num1)+int(num2))
    elif int(option)==2:
        print(int(num1)-int(num2))
    elif int(option)==3:
        print(int(num1)*int(num2))
    elif int(option)==4:
        print(int(num1)/int(num2))
        
#if we want to have it repeated only 3 times
i=0
while (i<3):
    option=input('please select your operator: 1. addition    2. substraction    3. multiplication    4. division   5. Exit :  ')
    if int(option)==5:
        break #before the start we can get out of the loop
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    if int(option)==1:
        print(int(num1)+int(num2))
    elif int(option)==2:
        print(int(num1)-int(num2))
    elif int(option)==3:
        print(int(num1)*int(num2))
    elif int(option)==4:
        print(int(num1)/int(num2))
    i=i+1

