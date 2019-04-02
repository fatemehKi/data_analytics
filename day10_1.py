#Introduction to Panadas

#The Series is the primary building block of pandas. A Series represents a one-dimensional labeled indexed array based on the NumPy array.

#


#pandas uses native python strings, which requires an "object" dtype.

import os
os.chdir(r'C:\Users\tjaber\Desktop\examples')

import numpy as np
import pandas as pd
#-------------------
#1) Series
#Creating series using collection
p1=pd.Series(np.random.random(size=4), index=['time1','time2', 'time3', 'time4'])
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
type(x)

x=p1[0]
x
type(x)


p2=pd.Series(np.arange(1,6), index=['t1','t2','t3','t4','t5'])
p2[['t3','t5']]
p2[[2,4]]

p3=pd.Series(range(11,15))
p3
p3=pd.Series(range(11,15), index=range(1,5))
p3
p3[0]#??

p5=pd.Series([1,"dd",4.5])
p5


p4=pd.Series({'age':35, 'income':60000, 'tax':20000})
p4
p4["age"]
#-------------------
#Creating series using a single value

p5=pd.Series('A')
p5[0]
type(p5[0])
#-------------------
A=np.repeat('t',9)
A
B=list(np.array(range(1,10), dtype=np.str))
B

for i in range(0,9):
    B[i]=A[i] + B[i]
    
B 
    
X=pd.Series([2,3,3,4,np.nan,2.1,np.nan,2,1], index=B)

print('Data:\n', X)  
X  
X.unique()

X.value_counts()#
X.count()#

X.tail(n=2)
X.head()
X.values
X.index
#-------------------
#a Python program to convert a Panda module Series to Python list
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))

#--------------------
#a Python program to compare the elements of the two Pandas Series.
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)
#---------------------

#2) DataFrame
#---------------------
#-Read a Data Frame from csv files.
coffee=pd.read_csv("coffee_info.csv", na_values='NA')
type(coffee)
coffee.shape
coffee.ndim
coffee.size
coffee.head(10)
x=coffee["Age"].head()
x
type(x)

x=coffee[["Age","Gender"]]
x
type(x)

coffee['Age'].dtype

coffee1=pd.read_csv("coffee_info.csv", na_values='NA', 
                    usecols=['Person_ID', 'Age', 'Income', 'Cups_Per_Week'], 
                    dtype={'Income':np.float64})
coffee1.head(10)

coffee2=pd.read_csv("coffee_info.csv", na_values='NA', 
                    usecols=[0,2,3,6], header=0, 
                    names=['uid', 'AgeGrp', 'Sex', 'Income'])
coffee2.head(10)

coffee3=pd.read_csv("coffee_info.csv", na_values='NA', 
                    usecols=[0,2,3,6], header=0, index_col=[0])
coffee3.head(10)
#-----------------------
#-Write a Data Frame to csv files.
x=pd.read_csv("coffee_info.csv", usecols=['Education', 'Age'], 
              na_values='bachelors')
x.head()
x['Education']=x['Education'].str.replace(" ","#")
x.to_csv("coffee_hash.csv", index=False)
#-----------------------
#Sub Data Frame

coffee1=pd.read_csv("coffee_info.csv", na_values='NA', 
                    usecols=['Person_ID', 'Age', 'Income', 'Education'])
coffee1.head()

coffee1[1:3]#rows
coffee1.loc[1:3]#rows, includes last index
coffee1.iloc[1:3]#rows, ignores last index

          

coffee['Age'].head()#series
coffee[['Age']].head()#data frame
type(coffee['Age'].head())
type(coffee[['Age']].head())

coffee1[['Age', 'Income']].head()


coffee1.iloc[[0,1,3],[0,1,2,3]]#columns indexes
coffee1.loc[[0,1,3],['Age', 'Income']]#columns names

coffee1.iloc[0:5, 1:4]
coffee1.iloc[0:5,:]#range indexes for both
coffee1.loc[[0,5],:]#selected indexex for rows

coffee1[['Age', 'Income']][0:3]#rows indexes: range
coffee1[0:6][['Age', 'Income']]#rows indexes: range
#----------------------
coffee1.Age>40
#Update data frame
coffee1['NetIncome']=coffee1['Income']*0.7
coffee1.head()
coffee1['Date']='25-June-2018'
coffee1.insert(1, 'Time', '08:30:40')

a=pd.concat([coffee, coffee1], axis=1)
a.shape
a.head()

s=coffee.sort_values(['Age'])
s.head()

s=coffee.sort_values( by= 'Age', na_position='first')
s=coffee.sort_index(axis=1)
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

























 





