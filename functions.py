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
- the inner function can not be calledr out of the outer function and when we call the outer function the inner func
- Lambda function is similar to the inlije finction and we have the 'Lambda' keyword.. it does do the print as well:
    foo = lambda arg1, arg2: functionlity
- lambda function insied the function requires attention for calling
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

# we created confusion on y ######## we can't have different name for a and b###### and c is considered a global variable for the internal function
def outfunc(a,b):
    x=a+b
    c =1
    def infunc(x,y):
        return(x-y+c)
   y= infunc(a,b)
   return(x*y)
print 

#the variables in the outer functions are like the global variables for the inner function;
#we are unable to call the inner function out of the outer function
def outer (num1):
    x=10
    def inner_increament(num1):
        return num1+x
    num2 = inner_increment(num1)
    print(num1, num2)

#local vs global variables
def outer (num1):
    x=10
    def inner_increament(num3):
        return num1+x
    num2 = inner_increament(num1)
    print(num1, num2)

outer(10)

##### scalling.. how to pass a list of values rather that scaled value in the function

def stdrange(inputlist):
    result = inputlist[:]
    print("the original list"+str(result))
    for j in range(0,11):
        result[j]=((inputlist[j])-min(inputlist))/(max(inputlist)-min(inputlist))
        #result[j]=(float(inputlist[j])-min(inputlist))/(max(inputlist)-min(inputlist)) this is correct too
    print ('the new list is ' + str(result))
    return(result)

x= stdrange(list(range(1,12)))
x=stdrange([1.2, 2.3, 4.0, 4.5, 3.1, 1.7, 2.2, 3.4, 5.0, 9.0, 7.4])

####lambda function
a = lambda r:3.14*r*r 
a(5.2)
#with two args
b = lambda x,y:x+y
b(1,10)

#arguments can be passed directly
def PrintMax(a,b):
    if a>b:
        print(a, 'is Max')
    elif a==b:
        print(a, 'is equal to ', b )
    else:
        print(b, ' is maximum')

PrintMax(3,4)

# Lambda function inside the 
def myfunc(n):
    return lambda a : a * n

#mydoubler is working like lambda function

mydoubler = myfunc(2)
mydoubler
mydoubler(11)

 

