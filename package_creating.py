# -*- coding: utf-8 -*-
"""
Spyder Editor
Authir: Fatemeh
This is a temporary script file.
"""
''' 
---Creating a package with methods '
 1. create a directory
 2. crete python module under the directore.. meaning creating the file(s) with the names of the 
 3. write the file __init__.py this name indicatesd that it is the python package
- 

'''

#------ creating the directory
import os
os.getcwd()#checking the current working directory
os.chdir(r"C:\Users\mfatemeh\Desktop\python") #changing direcriey and switch to the new directory
os.getcwd()
#if you want to create a folder in the current directory
os.mkdir("rectangle")
os.getcwd() # we are still in the same directory

#------using the created packages
import rectangle
width=15
length=20
myarea(width,length)
Perimeter(width,length)

#------- in 3 different files with the important name specifid 

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:35:53 2019

@author: mfatemeh.. __init__.py
"""

from rectangle.myarea import myarea
from rectangle.Perimeter import Perimeter

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:22:18 2019

@author: mfatemeh.. myarea..
"""
#the name of the function should match with the same name as the file
def myarea(L,W):
    print("The area is ", L*W)
    return(L*W)
    
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:25:47 2019

@author: mfatemeh... Perimeter
"""

def Perimeter(L,W):
    print("The Perimeter is ", 2*(L+W))
    return(2*(L+W))
