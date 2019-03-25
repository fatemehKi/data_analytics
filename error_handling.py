# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:02:41 2019

@author: mfatemeh
"""

''' 
- we can not convert the string to integer if thr value is character
- in the try whenever we get the error we jumpt to the except.. 1. try-except method
2. using the assert for passing a warning message if the condirtion in the assert is not correct 

'''

#- in the try whenever we get the error we jumpt to the except
while True: #there is no limitation of looping .. run until break
    try:
        x = int(input("Plesae enter a number"))
        break
    except ValueError:
        print('OOPs!')

# else is if the except is not true
num=(1,0,2,0,3,4)
for j in range(1,6):
    try:
        rate= (num[j]-num[j-1])/num[j-1]
    except ZeroDivisionError:
        print("division to zero")
    else:
        print('the changing rate is' +str(rate))
        

student = {'name':'John', 'gender':'Male', 'Mark':85, 'age':21}
for item in ('education','gender', 'age'):
    try:
        k=student[item]
        k=k+5
    except KeyError:
        print('No such a key '+item)
    except Exception:
        print('operation is wrong')
    else:
        print('outcome is ' + str(k))
        

def kelvinToFarenheit(temp):
    assert(temp>=0),"Colder than absolute zero!"
    return(temp-273)

print(kelvinToFarenheit(273))
print(kelvinToFarenheit(505.05))
print(kelvinToFarenheit(-5))


def changerate(L):
    for k in range(1,6):
        try:
            assert(L[k-1]>0)
        except AssertionError:
            print('error!division by zero')
        else:
            Y=100*(L[k]-L[k-1])/L[k-1]
            print(str(Y)+ '%')
            
changerate([0.23, 0.37, 0, 0.43, 0, 0.32])
