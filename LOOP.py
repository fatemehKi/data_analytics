# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:48 2019

@author: mfatemeh
"""
'''
- the default copying in the python is copy by reference therefore the change happenes everywhere
- inednting shows the loop body beginning and end
- the ++ or -- operator doesn't work in python
- the length of the loop needed  to be defined in the while
- append add the value at the end pf the list but if we want to add at the specific location we use insert
- extend
- remove('specific') will navigate through the list and remove that specific character. it does not give you the result
- pop(i) will remove the index i and returns the result
- push() 
- stack FIFO
- the append operator doesn't come in the print function print(append.list('me')); the reason is that we have to append and 
then we can print 
- xrange is in python 2 not in 3
- in the ranking we don't change the location but in sorting we cahnge the locatio
'''

squares=[1,4,9,16]

sum=0
for num in squares:
    sum+=num
print(sum) #we get the total once after the loop finished

sum =0   
for num in squares:
    sum+=num
    print(sum) #we get the value in every step


for i in range(10):
    print(i)
    

a=[2,4,6,8]
i=0

while i < len(a):
    print(a[i])
    i=i+1

list = ['larry', 'curly', 'moe']
list.append('shery') #if we append a list to the list above that will create a nested element
list

list.append(['aftemeh','nemo'])
list

list.insert(2,'mine')
list

list.extend(['ahmad', 'kian'])
list


print(list)
print(list.index('kian'))

list.remove('curly')
list

list.pop(3)#third  index been removed and the rest are 
list

#if we want to get the value that been removed, we need to define it
x=list.pop(1)
x
print(list)

a=range(3)
print(a)

#-----
data=[2,6,1,4]

[x for x in data] #numebric output 

[x<3 for x in data] #the boolean output

[x for x in data if x<3] #the numeric value, subset of the data with an specific condition

#if we are dealing with the data frame we can have something likein [nf.specific_colum ]

y=sorted(data)
data
y

#to descennding the 
y=sorted(data, reverse=True)
data
y







