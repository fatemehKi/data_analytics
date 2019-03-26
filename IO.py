# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:38:45 2019

@author: mfatemeh
"""

'''
- the built in functions are good for unstructured data base but packages are good for the structured data set
- unstructured data are like the essay in the public area.. 
- accessing the file
- file object = open(file_name [, access_mode] [, buffering]) or object = opem (file_name, access_mode)
- by default the access mode is r (read only) for binary format r+ is read and write
- it is safer to use r than w
- we don't have spftspace in python 3
- attributes are different than functions.. functions are doing something but attributes are not doing anything just returning status
- methods vs functions: methos are 
- to close the file we use object.close()
- the methos like close() will do an action but attribute lile closed will give a boolean showing the file is oprn or not
- if we have the same name it will overwrite with the last file so use diferent object name with different file
- to rename or remove the file, we need to close the file using ob1.close() and check ob1.closed and make sure the result is True
- with the write we have to be careful because it does overwrite.. we use w mostly if we are creating the file from the beginnig
- if we already have the file it is better opened with r other wise if we do create it it 
- if you try to open a non existing file with w+ it will create 
'''
##########Reading mode######
import os
os.chdir(r'C:\Users\mfatemeh\Desktop\python')
os.getcwd() # to amke sure we are in the above selected dir
# ob1 is asssociated to my text file.. I can access to my file using ob1
ob1= open('text.txt') # if the file does not exist we will get error
ob1.name # gives the name with the extension
ob1.mode #gives r because the default mode is r

ob1.closed
ob1.close()
ob1.closed
ob1.name # showing the object is still exsits even if we close it
ob1.mode

ob1 = open ('text.py') # the ob1 is chan

ob1= open('text.txt')
read_data=ob1.read() # reading the whole text file
read_data
type(read_data) # the type of the read_data is string

ob1.read(50) # if we have read the file before; then we get nothing at the end so we will turn it back to 0 by seek
ob1.seek(0,0) # the value it passed is the location 
ob1.read(50) # now we get the first 50 and if we run it again we will get the next 50 character-- read and move

ob1.tell() # showing the current location of us in the file

ob1.readline() # reading the current line to the next line.. you can read line by line
        
read_data.split()

ob1.close()
os.rename('text.txt','text2.txt') # changing the name of the file -- we need to make sure the file is been closed using ob1.close()
os.remove('abc.txt') # to remove the file not to the recyclebin

os.rename('text2.txt','text2.py')  # we can even change the extension

os.rename('text2.py','text.txt') 

#################Writting mode####
ob2=open('text2.py', 'w+') # tho old txt in the test2.py will be overwritten by this line
ob2.write(read_data) # it will return the number of charactres and after open /close the file we will see the result
ob2.close()
ob2.closed # if we manually open it we will see the changes

ob3=open('test3.py','w+') # we are creating or overwritting with empty
ob4=open('test4.py', 'r') # error because we don't have the file 
ob6=open('test5.py', 'r+') #error will read first.. therfore, error
ob5=open('test4.py', 'a') # will cretae the file but we are not overwritting.. it is writting mode firts
ob3.write('Hello Word')
ob3.write('Hello Word\n')
ob3.write('Hello Word\n') # we have to close it and 
ob3.close()
# and if we open it manually we will see 


for line in open('text2.py'):
    print(line, end='' ) # we get nothing in the end of each line
    
for line in open('text2.py'):
    print(line ) # we get the line (default type)

for line in open('text2.py'):
    print(line, end='*****' )

lst = [10, 20, 23, 4,56 ]
for x in lst:
    print(x, end = '\n') #----- that is the default === print(x)

lst = [10, 20, 23, 4,56 ]
for x in lst:
    print(x) 

def summ(x,y=7): #meaning that the second argument is optional and we can give it or not if we did give it will use the the given otherwise it will use the optinal 
    return(x+y)

# we can not have the optional before mandatory
def summ2(x=7,y): # error.. this is wrong.. because the non-default argument follows default argument
  return(x+y)

summ()#error because we need the X to be passed
summ(3) # the option value of y is used
summ(4,5) 

summ2(3)

# open function required argumern and without that we get the error
open() #error


summ3(x=6, y=5)
  return(x+y)

summ3(y=2) # here because y is not global variable we can not use it this way


