# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:30:29 2018

@author: Tareq
"""
import os

os.chdir(r'C:\Users\tjaber\Desktop\examples')

os.getcwd()
os.mkdir("newdir")
os.chdir("newdir")
os.rmdir("newdir")

#---------------------------------

ob1 = open("text.txt")
ob1 = open("text.py")
ob1.name
ob1.mode
#ob1.softspace
ob1.closed
ob1.close()

read_data=ob1.read()
read_data
type(read_data)
ob1.read(50)
ob1.readline()
ob1.tell()
ob1.seek(0,0)

import os
os.rename("test1.py","test3.py")

os.remove("abc.txt")

ob3 = open(r'C:\Users\tjaber\Desktop\examples\rectangle\area.py')


ob2 = open("test2.py", "w+")
ob2.write(read_data)
ob2.close()

ob3 = open("test4.py", "w+")
ob3.write("Hello world")
ob3.write("Hello_world\n")
ob3.close()

ob4 = open("test5.py", "w")

ob5 = open("test6.py", "a")

ob6 = open("test7.py", "a+")

#--------------------------
for line in open("test2.py"):
    print(line, end='')


lst=[10,5,7,45]
for x in lst:
    print(x, end='\n')
    
    
def summ(y=8,x=6):
    return(x+y)   
    
summ(3,6) 
summ(10)   


#-----------------    
s = 'abc'
it = iter(s)
it    
next(it)
    
x=iter(range(1,5))
x.__next__()
#----------------------------
#Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data.
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
 for char in reverse('golf'):
        print(char)
#----------------------------------------
def mygen():
    for x in range(10):
        yield x+2

gen=mygen()
next(gen)  
#--------------------------------
mygen2=(x+2 for x in range(10))      
next(mygen2)       
#------------------------------

def mygen3(x):
    for i in x:
        print(i+2)

mygen3(range(10))



#a Python program to read an entire text file.
def file_read(fname):
        global txt 
        txt = open(fname)
        print(txt.read())
        txt.close()
        return(txt.closed)
        

file_read('text.txt')
txt.closed
txt.close()
#------------------------------
#a Python program to read first n lines of a file.
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
                        
file_read_from_head('text.txt',3)

#---------------------------------------
# a Python program to append text to a file and display the text.
def file_read(fname):
        from itertools import islice
        with open(fname, "a") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
        
file_read('abc.txt')
#---------------------------------------
#a Python program to read a file line by line and store it into a list.
def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)
                print(type(content_list))
                return(len(content_list))

file_read("text.txt")
#--------------------------------------
#a python program to find the longest words.
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('text.txt'))
  

#--------------------------------------
#a Python program to count the number of lines in a text file.
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("text.txt"))
#--------------------------------------
#a Python program to count the frequency of words in a file.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("text.txt"))
#--------------------------------------

# a Python program to write a list content to a file.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def write_list(fname, lst):
    with open(fname, "w") as myfile:
        for c in lst:
                myfile.write("%s\n" % c)#The %s token allows to insert (and potentially format) a string. The %s token is replaced by whatever you pass to the string after the % symbol.


write_list("abc.txt",color)



content = open('abc.txt')
content.close()
print(content.read())
#----------------------------

f=open("abc.txt")
x = f.readlines()
x

x= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in x:
    print(i)






#---------------------------------------
#Copying file to another
from shutil import copyfile
copyfile('test1.py', 'abc.py')
#---------------------------------------

#a Python program to get the file size of a file.
def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of the file: ",file_size("text.py"))

#---------------------------------------
#a Python program to combine each line from first file with the corresponding line in second file.
with open('abc.txt') as fh1, open('abc.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):#zip is an iterator that aggregates elements from each of the iterables.
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
#---------------------------------------
#a Python program to remove newline characters from a file.
def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("text.txt"))
#---------------------------------------  

file = open("text.txt")
data = file.read()
print (data)
file.close()  # It's important to close the file when you're done with it

with open("text.txt") as file: # Use file to refer to the file object

   data1 = file.read()

#   do something with data

#Notice, that we didn't have to write "file.close()". That will automatically be called. 







