# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:51:34 2019

@author: mfatemeh
"""

'''
-------------Dictionary
- dictionary are defined by the {} and they have two parts:key and value, they are seperated using :
- we can define key using these two methods: 1. using {a:b, c:d } and 2. using dict()
- keys in dictionary are immutable but their values are mutable
-------------SET
- set are created using the [] syntax therefore the list syntax.. 1. we make set using a=set([]) and the other way is c={a,b,c}
- {} is the syntacs for the set and [] for the list
- set makes the value unique; even we add a repeated value it just re
'''

'''----- Dictionry------'''
X={'size':18, 'color':'green'} #size is the key and 15 is the value


Y1=dict((('size','color'), (18,'green'))) #it doesn't work the correct  way is like be
Y2=dict(size=18,color='green') #please be careful that we don't use the quotation in the strings here, 
Y1
Y2 #since we are refrencing using the keys, the order doesn't matter 

#to access the value rather that index in the lusr we use the keys
Y2['size']
#if the key does not exists in the list wer get the key error

Y2['fff']#error

#however, if we can assign a value to the non existing key, we will append the value and the keys to the list
Y2['fff']='mine'
Y2

#nd if we write the new values on the keys (that are immutable) the values get updated
Y2['size']='ggg'
Y2

#we can do arithmatic operation on the values as well
X['size']=X['size']+20
X

Y2.keys() # to get the keys
Y2.values() # to get the 

del Y2['fff'] #will delete the single element from dictionary based on the key value
Y2

del Y2 #the dictionary even the name wont exist any more

Y2.clear() #will clear the values but dictionary is still there however, delete will delete the total dictionary

'''--------------------SET____'''
country1=set(['USA', 'JAPAN', 'ENGLAND', 'USA', 'China', 'JAPAN'])
print('A set of unique country names:', country1) #we will make it unique after setting the list

country1.add('German')
print('A set of unique country names:', country1)
country1.discard('Japan')

country4=set(['England', 'Russia', 'india'])
country1.update(country4)

country1.intersection_update(country4) #will update country1*********************
print('After intersection', country1)

even_numbers ={2,4,6,8, 10}
big_numbers = {6,7,8,9,10}

#the below is one way (not the method way) of doing some logical operation
# to get he uncommon values 
print(big_numbers-even_numbers)

#union of two sets.. no repeating
print(big_numbers | even_numbers)

#intersection numbers which are big and even
print(big_numbers & even_numbers)

#numbers which are big or even but not both
print(big_numbers ^ even_numbers)

A={2,4,6,8}
B={6,8,10,12}

A | B
A.union(B)

A & B
A.intersection(B) #will not update A and there return value*********************

A - B
A.difference(B)

A ^ B
A.symmetric_difference(B)

A <=B
A.issubset(B) #logical output

A>= B
A.issuperset(B) #logical output
