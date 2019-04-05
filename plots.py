# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 00:48:07 2018

@author: Tareq
"""
'''
- two ways of creating dataframe 1. using the dataframe syntax and read_csv. read_excel
- line is the default graph type for the plot method
- tareq.j@metroc.ca
'''

import os
os.chdir(r'C:\Users\mfatemeh\Desktop\python')

import pandas as pd
import numpy as np
from sklearn import preprocessing

#reading excel
file1=pd.read_excel('scimagojr-3.xlsx',sheet_name='Sheet1', index_col=0, na_values=['NA']) # we use col=0 as the index
file1.head()

file1.loc[[1,2,3,4,5],['Country']]
file1.loc[[5],['Country']] # reading an specific row with specif column


#writing to excel
df_out = pd.DataFrame([('string1', 1),('string2', 2),('string3', 3)],
                       columns=['Name', 'Value'])
df_out
     
df_out.to_excel('tmp.xlsx')

pd.read_excel('tmp.xlsx')

pd.read_excel('tmp.xlsx', dtype={'Name':str, 'Value':float}) # not supported in my lap top

pd.read_excel('tmp.xlsx', converters={'Name':str, 'Value':float}) #since above does not work  

pd.read_excel('tmp.xlsx', na_values=['string1', 'string2']) # we specifi any string we want as na_value

#skipping rows with comment
df = pd.DataFrame({'a': ['1', '2', '4'], 'b': ['#2', '#3', '#5']})
df.to_excel('tmp2.xlsx', index=False) #we don't want to have indexes
pd.read_excel('tmp2.xlsx')
pd.read_excel('tmp2.xlsx', comment='#') # we specify that the string after hash is comment even the third column(if there was any)

df = pd.DataFrame({'a': ['1', '2', '4'], 'b': ['#2', '#3', '#5'], 'c': ['1', '2', '4'], 'd': ['#2', '#3', '#5']})
df.to_excel('tmp2.xlsx', index=False) #we don't want to have indexes
pd.read_excel('tmp2.xlsx')
pd.read_excel('tmp2.xlsx', comment='#') 

df = pd.DataFrame({'a': ['#1', '#2', '#4'], 'b': ['2', '3', '5']})
df.to_excel('tmp2.xlsx', index=False)
pd.read_excel('tmp2.xlsx', comment='#') #everything after hash key in one row is ignored
 
#--------------------------------
#Plotting 

#Matplotlib is the whole package; matplotlib.pyplot is a module in matplotlib; 
#and pylab is a module that gets installed alongside matplotlib.


import matplotlib.pyplot as plt

plt.interactive(False)#interactive mode is off, you have to call plt.show() explicitly to pop up figure window.

x = np.linspace(-2, 2, 100) #creating 100 values between -2 and 2

plt.plot(x, x, label='linear') #first cordinate is the x and the second is y.. we are not saving the plot to any object
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.show() # if we do plt.plot all at the samr time and then run 
#---------------------------
#Line chart

values = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9]
plt.plot(values)
plt.show() #showing that if we don't specify two arguments, the given value is considered to be  y and the index is used for the x axis

#Multiple line chart
sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
line_chart1 = plt.plot(range(1,12), sales1) #first argument is the x axis and the second argument is the y axis
line_chart2 = plt.plot(range(1,12), sales2)
plt.title('Monthly sales of 2016 and 2017')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.legend(['year 2016', 'year 2017'], loc=1) #loc is the location of the legend and the order is important and the first is for the first object and 
#the second argument is for the second object that been run
plt.legeInd(['year 2016', 'year 2017'], loc=4) #loc=4
plt.show()

#Line style
line_chart1 = plt.plot(range(1,12), sales1,'--') # the style is pased
line_chart2 = plt.plot(range(1,12), sales2,':')

#colour
line_chart1 = plt.plot(range(1,12), sales1,'g') # the colour type.. if we are adding more than one parameter, we need to specifiy with the parameter name like colour=
line_chart2 = plt.plot(range(1,12), sales2,'r')
line_chart2 = plt.plot(range(1,12), sales2, color='r', linestyle='--')
#the website to get the style and colour
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
#-----------------------------

#Pie chart
# we have to have values, colour and labe; values are the first parameter an dffthe 
values = [60, 80, 90, 55, 10, 30]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['US', 'UK', 'India', 'Germany', 'Australia', 'South Korea']
explode = (0.2, 0, 0, 0, 0, 0) #the US  that is the first value that and come out 
plt.pie(values, colors=colors, labels= values,explode=explode,
        counterclock=False, shadow=True)
plt.title('Population Density Index')
plt.legend(labels,loc=3)
plt.show()

#Percentage
plt.pie(values, colors=colors, labels=labels,
explode=explode, autopct='%1.2f%%', counterclock=True, shadow=True) # we put the autopct to show the percentage in the slice

#-----------------------------

#Scatter plot chart

weight1=[63.3,57,64.3,63,71,61.8,62.9,65.6,64.8,63.1,68.3,69.7,65.4,66.3,60.7]
height1=[156.3,100.7,114.8,156.3,237.1,123.9,151.8,164.7,105.4,136.1,175.2,137.4,164.2,151,124.3]
 
plt.scatter(weight1,height1,c='b',marker='o')#marker=’o’ denotes the type of plot  "O' is showing each in circle and 
#(. , o v ^ 8 s p D +)
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('scatter plot - height vs weight',fontsize=20)
plt.show()


#scatter plot for three different groups
weight1=[57,58.2,58.6,59.6,59.8,60.2,60.5,60.6,60.7,61.3,61.3,61.4,61.8,61.9,62.3]
height1=[100.7,195.6,94.3,127.1,111.7,159.7,135,149.9,124.3,112.9,176.7,110.2,123.9,161.9,107.8]
 
weight2=[62.9,63.1,63.2,63.3,63.4,63.4,63.4,63.5,63.6,63.7,64.1,64.3,64.3,64.7,64.8]
height2=[151.8,156.3,136.1,124.2,156.3,181.2,255.9,163.1,123.1,119.5,179.9,114.8,174.1,108.8,105.4]
 
 
weight3=[69.2,69.2,69.4,69.7,70,70.3,70.8,71,71.1,71.7,71.9,72.4,73,73.1,76.2]
height3=[166.8,172.9,193.8,137.4,162.4,137.1,169.1,237.1,189.1,179.3,174.8,213.3,198,191.1,220.6]
 
 
weight=np.concatenate((weight1,weight2,weight3)) #45 values
height=np.concatenate((height1,height2,height3))
len(weight)
len(height)
 
color_array = ['b'] * 15 + ['g'] * 15 + ['r']*15  # we need to cover all 45 values
 
plt.scatter(weight, height, marker='*', c=color_array)
 
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('grouped scatter plot - height vs weight',fontsize=20)
plt.show()
#----------------------------

#Bar chart

city=['Delhi','Beijing','Washington','Tokyo','Moscow']
pos = np.arange(len(city))
Happiness_Index=[60,40,70,65,85]
 
plt.bar(pos,Happiness_Index,color='blue',edgecolor='black')
plt.xticks(pos, city) #xtick uses the city for the pos.. without the xtick we will see 0,1,2,..
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Barchart - Happiness index across cities',fontsize=20)
plt.show()

#Horizontal Bar Chart
plt.barh(pos,Happiness_Index,color='blue',edgecolor='black')

#Stacked Bar Chart with legends:
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
Gender=['Male','Female']
pos = np.arange(len(city))
Happiness_Index_Male=[60,40,70,65,85]
Happiness_Index_Female=[30,60,70,55,75]
 
plt.bar(pos,Happiness_Index_Male,color='blue',edgecolor='black')
plt.bar(pos,Happiness_Index_Female,color='pink',edgecolor='black',bottom=Happiness_Index_Male) #the bottom parameters helping us to avoid the overlap
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Stacked Barchart - Happiness index across cities',fontsize=18)
plt.legend(Gender,loc=2)
plt.show()

#Overlapping!!
plt.bar(pos,Happiness_Index_Male,color='blue',edgecolor='black')
plt.bar(pos,Happiness_Index_Female,color='pink',edgecolor='black')


#Grouped Bar Chart with legends:
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
Gender=['Male','Female']
pos = np.arange(len(city))
bar_width = 0.35
Happiness_Index_Male=[60,40,70,65,85]
Happiness_Index_Female=[30,60,70,55,75]
 
plt.bar(pos,Happiness_Index_Male,bar_width,color='blue',edgecolor='black') #we pass the weigth to get the 
plt.bar(pos+bar_width,Happiness_Index_Female,bar_width,color='pink',edgecolor='black')
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Group Barchart - Happiness index across cities By Gender',fontsize=18)
plt.legend(Gender,loc=2)
plt.show()

#----------------------------------------------
#Box plot #ploting one numeric coloumns 

value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
 
box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data)
plt.show()


#box plot with fills and labels:    
bp=plt.boxplot(box_plot_data,patch_artist=True, labels=['course1','course2','course3','course4']) #to fill the box with the default colour
#argument patch_artist fills the boxplot
#bp is the object 

for x in bp['boxes']: #the Box inside the bp is the reserved key word for the 
    # change outline color
    x.set(color='red', linewidth=2) #this refers to the color of the outliner
    # change fill color
    x.set(facecolor = 'green') #this refers to the color of the box itself
    
    
#Horizontal box with different colors:    
box=plt.boxplot(box_plot_data,vert=0,patch_artist=True,labels=['course1','course2','course3','course4'],)
 
colors = ['cyan', 'lightblue', 'lightgreen', 'tan']
for patch, color in zip(box['boxes'], colors): #batch is the loop iterator fot box['Box'] and the color is the temp variable to go in colors
    patch.set_facecolor(color)
 
plt.show()    
    

#notch format of the box plot    
plt.boxplot(box_plot_data,notch='True',patch_artist=True,labels=['course1','course2','course3','course4'])    
#----------------------
#Histogram chart
#step type (no fills)
values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,bins=5, histtype='step', align='mid', color='g', label='Test Score Data') #5 is the number of bins the number of the steps is bins-1
plt.legend(loc=2)
plt.title('Histogram of score')
plt.show()

#bar type (with fills).
plt.hist(values,5, histtype='bar',
align='mid', color='c', label='Test score Data',edgecolor='black')
plt.legend()
#----------------------
#Create a DataFrame
#Filter/index

d = {
    'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
    'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
            'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
     
    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
 
df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

df['Name'] # accessing the column 

x=df['Score'].mean()
type(x)
x
z=df['Score']
type(z)

y=np.array(x)
type(y)
y
np.mean(y)
#therefore we have optioms of 



df[['Name', 'Score']]

df[:2]

df['Score'] > 70


df[df['Score'] > 70] #we get the subset of the data

df[(df['Score'] > 70) & (df['Score'] < 85)] 

df.ix[:,'Score'] # is the series

type(df.ix[:,'Score'])
#Indexing with .ix: 

df.ix[3,2] #one element 4th row and the 3rd column.. ix is similar to the iloc
df






#Normalisation
d = {
       'Score':[62,-47,-55,74,31,77,85,63,42,67,89,81,56]}
 
df = pd.DataFrame(d,columns=['Score'], dtype='float')
df

#Create a min max processing object
min_max_scaler = preprocessing.MinMaxScaler()
scaled_array = min_max_scaler.fit_transform(df)

df_normalized = pd.DataFrame(scaled_array)
df_normalized

    


#--------------------- 
d = {
    'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
    'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
            'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
     
    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Result':['Pass','Pass','Fail','Pass','Fail','Pass','Pass','Fail','Fail','Pass','Pass','Fail']}
 
df = pd.DataFrame(d,columns=['Name','Exam','Subject','Result'])
df


pd.crosstab(df.Subject, df.Result,margins=False) # the first argument needed to be categortical and the second can be numeric
# it does show the frequency 

pd.crosstab([df.Subject, df.Exam],df.Result, margins=True) #margin means to get the total(All) in each margin


