# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:04:58 2019

@author: mfatemeh
"""
'''
- string that the only variable type that we can iterate; that's why we can not iterate integer
- iter is special function in python that we get element by element. Tuples are iterable, in exactly the same manner as lists. 
- after the last iteration we get the StopIteration
- Since a tuple is iterable, a mutable copy is easily created using the list() builtin. t = ('Othello', 'Iago')
list(t) the result is ['Othello', 'Iago'].. we either have a scalar or we have the iterable variables
- generators are a simple and powerful tool for creating iterator.., generator is the way of using iterators
- to call the generator we either use the loop or we use the next()
- with is a secure way of reading and opening and closing at the end
'''

s='abc'
it = iter(s)# it is the iter object
it
next(it) #this is a built-in function 

x= iter(range(1,5))
x.__iter__() # this is a method and it does do exactly same as the next(it) but it is a method not 
#similary we can do below:
next(x)

#-----------Generator: coming with yield
    # first way of using the generator
def reverse(data):
    for index in range(len(data)-1, -1, -1): #stoping at zero that's why second value is -1 .. becuase the last one is 0
        yield data[index] 
# yield is send to output and go to the next.. using this way we can go inside the loop adn we get the value step by step
       

for char in reverse('golf'):
    print(char)

#--- second way of using generator
def mygen():
    for x in range(10):
        yield x+2
        
gen=mygen() #defining object
next(gen)
gen

next(mygen()) # doesn't work, we need to get the object

#--------
mygen2=(x+2 for x in range(10))
next(mygen2)

#------ using the lambda we get error because can not have it 
mygen3= lambda x: for i in x: print(i+2)

#---- we can get the result without controling the result and stepping into those..generator vs normeal
def foo(x):
    for i in x:
        print(i+2)

foo(range(10))

#------ a python program to read an entite txt file and close it if it is open

def file_read(fname):
    txt=open(fname)
    print(txt.read())
    return(txt.closed)


file_read('text.txt')
txt.closed # we get the error because the txt is defined inside the function 

def file_read(fname):
    global txt #######################we add this to get the txt outside
    txt=open(fname)
    print(txt.read())
    return(txt.closed)

file_read('text.txt')
txt.closed 
txt.close()

# or another way of closing the file is to do it inside the defined functions 
def file_read(fname):
    global txt
    txt=open(fname)
    print(txt.read())
    txt.close()
    return(txt.closed)

file_read('text.txt')
txt.closed 

#-------------super function-- we want to read specif number of lines-- slicing inside the file
def file_read_from_head(fname, nlines):
    from itertools import islice 
    with open (fname) as f:
        for line in islice (f, nlines):
            print(line)
    return(f.closed)

file_read_from_head('text.txt',2)



