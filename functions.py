# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:11:35 2019

@author: mfatemeh
"""

'''
- functions in the programming is defined as a sequence of statments and once we call them they will do certain tasks
and they facilitate the repeated actions
- each program has many in-built function like replace( , , ) and we don't see the internal 
- functions can return a value then we have to write a receiver variable name for it
- the syntax functions in python 
 def foo(args): --colon shows the start
     indenting is the must
     print...
     blah blah
     ..
     retun(variable)
not indent is showing the new part 
- in python 3 even if we don't have a print statment and we only have the return, it will automatically print the output
unless you save it in an specif variables.. i.e., if we put the return in the specific variables it will 
- unlike C++ if we assign the output as a variable; however, we don't have a return, we don't get error; however, we don't get anything
- in orfr to get the documentation inside a function (first line after the def ) we use print(foo.__doc__)
'''

def print_me(name, age):
    print('my name is ' + name + ' and I am ' +str(age))
    return(name+','+str(age))

x=print_me('larry',19)
x

def sumxy(x,y):
    z=x+y
    # print(z)
    return(z)
#one way of getting output
sumxy(4,5)

#another way
a=sumxy(4,5)
a

def sumxy(x,y):
    z=x+y
    print(z)
    #return(z)
sumxy(4,5) #showing the value; therfore it does have a return or print
a=sumxy(4,5) # if in this case it shows something then it is print for sure.. 
a

#### if out of the function we do have the variables similar to the insode
def sumxy1(x,y):
    '''my first func'''
    z=x+y
    # print(z)
    return(z)
z=10
z 
sumxy(4,5)
z

# to define the global variabl and make it changable insid similar to the outside.. it is not recommended
def sumxy(x,y):
    global z
    z=x+y
    print(z)
    return(z)

z=10
z
sumxy(4,5)
z

#getting the documentation
print(sumxy1.__doc__)
print(max.__doc__)



