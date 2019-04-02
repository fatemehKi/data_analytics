# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:05:52 2019

@author: mfatemeh
"""

'''
- series are the begiest and the main building block in data frame
- series are built as a numpy array
- we use the labela and index to refering the series.. 
- series are merging the feature of dictionary and the list
- in numpy the defult for the string change was 'b' bit
- in the series every columns needed to be one data type and therefore if we have multiple data 
type all comes in the output one data type (object)
- data frame is two dimensional series
- float is more generic than int and string is the omre generic than the others
- X.unique() # new output as the array
- X.value_counts() # frequency of each value; it also gives the values and the uniqe value acting like the index
- X.count() #missing values are not counted just giving the number of non-missing elements
- to get the limited record of the data.. the default first 5 numbers X.tail(n=2), X.head(n=2)        
- X.values getting the values of the list we can conver to numpy and them use numpy functions
- X.index getting the index of the list we can conver to numpy and them use numpy functions
- ds.tolist(), the output changd to the list
- two dimensional data sets are called data frames
- series a one dimension array but dataframe is combination of seeries [c1] gives us just series; however,[[c1]] keeps the data frame and gives us only a column of this
- the default nimeric values are float type
- lov vs iloc we get the index in the loc not in iloc
'''

import numpy as np
import pandas as pd

p1=pd.Series(np.random.random(size=4), index=['time1', 'time2', 'time3', 'time4']) #we are using the label or 
p1
type(p1)
p1.ndim
p1.shape
p1.size

x=p1[[0,1]]
x
type(x)

x=p1[[0]]
x

x=p1[0] #we don't get the series anymore, because it is refering to the scalar, we get the float
x
type(x)

x=p1[0,1] #we get error
x
type(x)

p2=pd.Series(np.arange(1,6), index=['t1', 't2', 't3', 't4', 't5'])
p2[['t3', 't5']] #equals to the below
p2[[2,4]]

p3=pd.Series(range(11,15))
p3=pd.Series(range(11,15), index=range(1,5)) # we can not have both the label and the index number
p3
p3[0] # error KeyError

p3_= pd.Series([1, 'dd', 4.5])
p3_ # the data type shows at the end of it

p4=pd.Series({'Age': 35, 'income':6000, 'tax': 2000})
p4
p4['Age'] # the output is an scalar type
p5=p4[['Age']] #this is a series type

#creating series using a single value
p5=pd.Series('A')
p5[0]
type(p5[0])

#------- __________________important
A=np.repeat('t',9)
A
B=list(np.array(range(1,10), dtype=np.str))
B

for i in range(0,9):
    B[i]=A[i]+B[i]
B

X=pd.Series([2,3,3,4,np.nan, 2.1, np.nan, 2,1], index=B)

B=pd.Series(range(0,9))
X=pd.Series([2,3,3,4,np.nan, 2.1, np.nan, 2,1], index=B)


Y=X.unique() # new output as the array
type(Y)

Y=X.value_counts() # frequency of each value; it also gives the values and the uniqe value acting like the index
Y[3.0]

Y=X.count() #missing values are not counted just giving the number of non-missing elements

#to get the limited record of the data.. the default first 5 numbers
Y=X.tail(n=2)
Y=X.head(n=2)        

X.values # we can conver to numpy and them use numpy functions
X.index  # we can conver to numpy and them use numpy functions

ds=pd.Series([2,4, 6, 8, 10])
ds
type(ds)
ds.tolist()
type(ds.tolist()) 

ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,10])
ds1
ds2
ds1==ds2
ds1>ds2
ds1<ds2

# the length needed to be the same and arherwise, we get error
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7])
ds1
ds2
ds1==ds2
ds1>ds2
ds1<ds2

import os
os.getcwd()
os.chdir(r'C:\Users\mfatemeh\Desktop\python')
coffee=pd.read_csv('coffee_info.csv', na_values='NA')
type(coffee)
coffee.shape
coffee.ndim
coffee.size
coffee.head()
x=coffee['Age'] # it is a series type; by default the row 0 is assumed to be column
type(x) # the type is the series and therefore a dataframe is a combination of the series
x=coffee[['Age']] # if we pass [[]] we get the dataframe a specific set.. we get subset by passinf [[]]; 
type(x) 
coffee['Age'].dtype #access the column Age and get the data type of the column age
coffee[['Age']].dtype #error because we don't have one type for the whole data frame

x=coffee[['Age', 'Gender']]
x=coffee['Age','Gender'] #error because we are expecting only one series

    
coffee1=pd.read_csv('coffee_info.csv', na_values='NA', 
                    usecols=['Person_ID', 'Age', 'Income', 'Cups_Per_Week'],
                            dtype={'Income':np.float64})   

coffee1.head(10)

x=pd.read_csv('coffee_info.csv', na_values='bachelors') #it will change all  bachelor to the nan

    
coffee1=pd.read_csv('coffee_info.csv', na_values='NA', 
                    usecols=range(0,2), header=0, #the default header is 0
                    dtype={'Income':np.float64})   

    
coffee2=pd.read_csv('coffee_info.csv', na_values='NA', 
                    usecols=[0,2,3,6], header=0,
                            names=['uid', 'AgeGrp', 'sex', 'Income'])  # the number od names should be the same numbers

coffee3=pd.read_csv('coffee_info.csv', na_values='NA', 
                    usecols=[0,2,3,6], header=0, index_col=[0])  # meaning use the first(0) column as the index.. should be unique in python 2 but 3 doesn't but wrong output               
# as can be seen in the output the first column is in lower level



coffee3=pd.read_csv('coffee_info.csv', na_values='NA', 
                    usecols=[0,2,3,6], header=0, index_col=[1]) # 1 here means number 2 in usecols[] value in the index_col is the index of the usecols; if we put 4 we get error 
# and the order is important


x=pd.read_csv('coffee_info.csv', usecols=['Education', 'Age'],
                    na_values='NA')
x.head()
x['Education']=x['Education'].str.replace(' ', '#')

x.to_csv('Coffee_hash.csv') # if we look at the file we will see that it does have a new column of the index
x.to_csv('Coffee_hash.csv', index=False) # we will remove the first column


coffee1=pd.read_csv('coffee_info.csv', na_values='NA', 
                    usecols=['Person_ID', 'Age', 'Income', 'Cups_Per_Week'],
                            dtype={'Income':np.float64})   

#slicing 
coffee1[1:3] # if we have a single bracket with the range it targets rows
coffee1.loc[1:3]
coffee1.iloc[1:3]



coffee['Age'].head()#series
coffee[['Age']].head()#data frame
type(coffee['Age'].head())
type(coffee[['Age']].head())

coffee1[['Age', 'Income']].head()


coffee1.iloc[[0,1,3],[0,1,2,3]]#columns indexes
coffee1.loc[[0,1,3],['Age', 'Income']]#columns names

# if we are passing the range we do not need double[[]]
coffee1.iloc[0:5, 1:4]
coffee1.iloc[0:5,:]#range indexes for both
coffee1.loc[[0,5],:]#selected indexex for rows

coffee1[['Age', 'Income']][0:3]#rows indexes: range
coffee1[0:6][['Age', 'Income']]#rows indexes: range

       
 #object type caling  that does not need quotation for Age       
coffee1.Age>40 # all values in row has the boolean

coffee.head()
coffee.Education
#equal to below
coffee['Education']

y=coffee[coffee.Education=='bachelors'] #gettinf subset from the coffee using the list comprehensuon 
y1=coffee[coffee['Education']=='bachelors' ]
len(y1)
y1.size # not 


#Update data frame
coffee['NetIncome']=coffee['Income']*0.7 # a new seris is created in right and been added ewith the given name in the 
coffee.head()
coffee['Date']='25-June-2018'
coffee.insert(1, 'Time', '08:30:40') # inserting a new column in an specific location

coffee.Age[coffee.Age>30]=0 # we change the 
             
a=pd.concat([coffee, coffee1], axis=1) #concatinating basesd on the columns (column_wise) meaning the columns are repeated 
a.shape
a.head()


a=pd.concat([coffee, coffee1], axis=0) #concatinating basesd on the rows (row_wise) meaning the columns are same and the rows are added
a.shape
a.head()
#the above results are not a correct  responses and we normally use the merge not concatination, if there is a column in one of them not in the other
# we need to deal with the missing values

s=coffee.sort_values(['Age']) # the amin file will not change in default is based on index and the result shows after sorting, the first index is 126 
s.head()

s=coffee.sort_values( by= 'Age', na_position='first') # the missing values are coming firstby is optional
s=coffee.sort_index(axis=1) #soritng of the column are changes and start from Capital to small alphabets
s=coffee.sort_index(axis=1, ascending= False)

#-----------------------------

data_url = 'http://bit.ly/2cLzoxH'
# read data from url as pandas dataframe
gapminder = pd.read_csv(data_url)
# print the first three rows
gapminder.head(n=5)

sort_by_life = gapminder.sort_values('lifeExp',ascending=False)
sort_by_life.head(n=5)


sort_by_life_gdp = gapminder.sort_values(['continent','lifeExp'])
sort_by_life_gdp.head(n=5)
#-----------------------------
