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
- therefore, the horizantal ranking only works for the heteregenous data frame
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

sort_by_life = gapminder.sort_values('lifeExp',ascending=False) #we are sorting based in the lifeExp column and in descending 
sort_by_life.head(n=5)


sort_by_life_continent = gapminder.sort_values(['continent','lifeExp']) #sorting based on two columns in asccending, first continent and then the lifeExp.. if we have three column , the first two needed to be the same
sort_by_life_continent.head(n=5)
#-----------------------------
pd=pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]], columns=['A', 'B', 'C'])
#df
#df.iat[1,2]

#ranking vs sorting is important in slide 24.. it is only works for numeric and the output is float
A=pd.Series([7,4,9, 6, 1, 6,0])
B=pd.Series([10, 72, 19, 160, 72, 8, 1])
C=pd.Series([0, 1, 0, 2, 0, 3, 5])
D=pd.DataFrame({'col1':A, 'col2':B, 'col3':C})
D.rank() # the 'ties' are assignede method='average' default rank
D.rank(axis=1)
D.rank(ascending=False, method='first') 
D.rank(pct=True) #calculates the percentagerank, i.e. pct rank=rank/maximum_value of the rank

     
#---------------------------
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],columns=['A', 'B', 'C'])
df
df.iat[1, 2]
df.iat[1, 2] = 10
df
df.loc[0].iat[1]

df.at[2, "A"]
#----------------------------
#Ranking

d = {
'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
'History','History','History','Economics','Economics','Economics'],
'Score':[62,47,55,74,31,77,85,63,42,62,89,85]}
 
df = pd.DataFrame(d,columns=['Name','Subject','Score'])
df

# to get the correlation of two columns
pd.crosstab(df.Name, df.Subject)

df.info()

df.rank()#Average(default)
df.rank(pct=True)#percentage rank
df
df.rank(axis=1) # ignored the string and just rank the last column with itself then the result is the just one

xx=df.rank(pct=True)#percentage rank
xx.rank(axis=1)#column wise

d = {
'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
'History','History','History','Economics','Economics','Economics']}

 
yy = pd.DataFrame(d,columns=['Name','Subject'])
yy
yy.rank(axis=1)  # if all dataframe is string then the axis=1 has meaning.. therefore, the horizantal ranking only works for the heteregenous data frame


df['score_ranked']=df['Score'].rank(ascending=1)#average-asc# new column is created and we are ranking the single column
df['score_ranked']=df['Score'].rank(ascending=0)#average-descending order
df['score_ranked']=df['Score'].rank(ascending=0, method='min')#minimum---using the minimum ranking for the two similar value and we leave one ranking numbers in between
df['score_ranked']=df['Score'].rank(ascending=0, method='max')#maximum-- using the maximum ranking for the two similar value and we leave one ranking numbers before 
df['score_ranked']=df['Score'].rank(ascending=0, method='dense')#dense-- using the mimimun ranking for the two similar value and but we don't skip-leave the empty any ranking
df['score_ranked']=df['Score'].rank(ascending=0, method='first')#first--  assign the first ranking to the first appearence in the similarities
df
#----------------------
#Ranking by group-- we do ranking inside the subject

df["group_rank"] = df.groupby("Subject")["Score"].rank(ascending=1,method='dense')
df
df['Subject'].unique()
#----------------------
#similar to the list comprehension , applying a acondition to a column
a=(df.Score>79) #a is one column=> it is a series
a
a=(df.Score>40) & (df.Name>'B') #meaning that anything after B like Bob is ok
df.Score[a==True] # we are comparing the boolean value of the same location; however, it is not in the data farme parts

df.Score[df['Score']>79] #slicing 
#----------------------

#Merge

# data frame 1
d1 = {'Customer_id':pd.Series([1,2,3,4,5,6]),
  'Product':pd.Series(['Oven','Oven','Oven','Television','Television','Television'])}
df1 = pd.DataFrame(d1)
 
 
# data frame 2
d2 = {'Customer_id':pd.Series([2,4,6]),
    'State':pd.Series(['California','California','Texas'])}
df2 = pd.DataFrame(d2)
df1
df2

#inner join in python pandas
pd.merge(df1, df2, on='Customer_id', how='inner')

pd.merge(df1, df2, how='inner') # because they do have the same name for customer_ID; it will take it for the join

        
# data frame 3
d3 = {'Customer_id3':pd.Series([2,4,6]),
    'State':pd.Series(['California','California','Texas'])}
df3 = pd.DataFrame(d3)       
        
pd.merge(df1, df3, how='inner')# because they do not have the same name this will not work
        
# outer join in python pandas
pd.merge(df1, df2, on='Customer_id', how='outer') # it is used to find out the problema and missing values

# left join in python
pd.merge(df1, df2, on='Customer_id', how='left') #give me everything from the left(df1) and the commons from the right (df2)
pd.merge(df2, df1, on='Customer_id', how='left') #give me everything from the left(df2) and the commons from the right (df1)


# right join in python pandas
pd.merge(df1, df2, on='Customer_id', how='right')
pd.merge(df2, df1, on='Customer_id', how='right')
#------------------------
#Pivot: Reshape long to wide
d = {
    'countries':['A','B','C','A','B','C'],
    'metrics':['population_in_million','population_in_million','population_in_million',
                             'gdp_percapita','gdp_percapita','gdp_percapita'],
    'values':[100,200,120,2000,7000,15000]
    }

df = pd.DataFrame(d,columns=['countries','metrics','values'])
df

# reshape from long to wide in pandas python #use the unique value of the countries as the new index and 
df2=df.pivot(index='countries', columns='metrics', values='values')
df2
type(df2)
df2.to_csv('new.csv')

#------------------------
#reshape using stack and unstack/Multilevel indexes

header = pd.MultiIndex.from_product([['Semester1','Semester2'],['Maths','Science']])
d=([[12,45,67,56],[78,89,45,67],[45,67,89,90],[67,44,56,55]])
 
 
df = pd.DataFrame(d,
                  index=['Alisa','Bobby','Cathrine','Jack'],
                  columns=header) # the header is multi levels and the second level repeated for all level1
df


#Stack() Function in dataframe stacks the column to rows at level 1 (starting from 0)(default).

stacked_df=df.stack() #reducing the level -- m
stacked_df

#unstack() Function in dataframe unstacks the row to columns . Basically it’s a reverse of stacking

unstacked_df = stacked_df.unstack()
unstacked_df

#Stack the dataframe at level 0

stacked_df_lvl=df.stack(level=0)
stacked_df_lvl
#-------------------------

#Re-indexing: change order of row and column in pandas-- smart way of handling missing

d = {'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine','Rahul','David','Andrew','Ajay','Teresa'], 
'Score1':[62,47,55,74,31,77,85,63,42,32,71,57],'Score2':[89,87,67,55,47,72,76,79,44,92,99,69], 
'Score3':[56,86,77,45,73,62,74,89,71,67,97,68]}
 
df = pd.DataFrame(d)
df

#reindex or change the order of rows
df.reindex([8,11,9,2, 1, 0,7,5,6,4,10,3]) # we simply can remove a row by removing its index without error

df.reindex([8,11,9,2, 1, 0,7,5,6,4,10])

# reindex or change the order of columns
columnsTitles = ['Score2', 'Score1', 'Score3']
df.reindex(columns=columnsTitles) # we get the new order of the columns 

df.reindex([8,11,9,2, 1, 0,7,5,6,4,10], columns=columnsTitles)# new order for the indexes

#--------------------------------

#missing values
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], #five rows and five index
columns=['one', 'two', 'three']) # three columns with three names
df
df['four'] = 'bar'
df['five'] = df['one'] > 0 # we adding a boolean column
df
#df[df['one']<0]

# inserting the missing value for the columns
df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) #passing the indexes that are not available in the df
df2
pd.isnull(df2['one']) # the single column as the boolean series
df2['four'].notnull() # a series that opposite of isnull
df2.isnull() #data frame of the boolean value

df2.count() # the number ofo non missing values

df2[df2['five'].notnull()] # in the data frame missing rowsin the 'five' is removed
df2['five'].notnull() # is a series
df2


#--------------------------------
#Drop the duplicate rows: based on the primary key

d = {
'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine','Alisa','Bobby','kumar','Alisa','Alex','Cathrine'],
    'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
    'Score':[85,63,55,74,31,77,85,63,42,62,89,77]}
 
df = pd.DataFrame(d,columns=['Name','Age','Score'])
df

# drop duplicate rows--- we will be removing the duplication rows (remove the duplication in the whole row)
df.drop_duplicates()
df.drop_duplicates(keep='last')# remove the duplication but keep the last one

# drop duplicate by a column name
df.drop_duplicates(['Name'], keep='last')#removing duplication just in one column.. be careful that the column required to be a primary key
# we always remove the whole row

df["is_duplicate"]= df.duplicated() # it a boolean function and check if it is repeated or no
df

# Drop an observation or row
df.drop([1,2]) #row index 1 and 2 is dropped.. the default axis for the column is 0 meaning it removes rows
df.drop((3:8)) #error -- range does not work
df.drop([3:8]) #error -- range does not work
df.drop(df.index[3:5])

# Drop a row by condition-- list comprehension
df[(df.Name != 'Alisa') & (df.Age <23)]
df2=df[(df.Name != 'Alisa') & (df.Age <23)]
df2
#if we want to change the index and make it in order
df2.index=[0,1]
df2

# Drop bottom 3 rows #3rd method and without using function or condition
df[:-3]

# drop a column based on name
df.drop('Age',axis=1) # if we want to remove the column we need to have axis=1
df
# drop a column based on column index # if we don't remember the column name
df.drop(df.columns[2],axis=1)

del df['Age']#!!!  The output is permanently deleting
df

#---------------------------------
#drop na in specific location 
df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1],
         [np.nan, np.nan, np.nan, 5]],
  columns=list('ABCD'))
df


df.dropna(axis=1, how='all') #we are moving columns.. if all values in the column is na drop that column
    
df.dropna(axis=1, how='any') #any column yjat have at least one missing value dropped
    
df.dropna(axis=0, how='all') #move horizantaly.. we delete when whole row is nan
df.dropna(axis=0, how='any') #move horizantaly.. we delete when whole row is nan.. all rows have at least one nan

df.dropna(thresh=2) # the value is showing the number of non-missing value you should have in record to keep the record
df.dropna(thresh=3) 

df.dropna(thresh=3, axis=1) 

#--------------------------------
 
#Create a Dictionary of series
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
      'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}
 
df = pd.DataFrame(d)
df

#row wise mean-- we can apply the aggregate functions-- any aggregate function
df.apply(np.mean,axis=1)    
   
np.mean(df.Score_Math)
np.mean(df['Score_Math'])
#column wise meanprint  
df.apply(np.mean,axis=0)


df.apply(np.max,axis=1)       
