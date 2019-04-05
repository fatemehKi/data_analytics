# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 00:48:07 2018

@author: Tareq
"""

import os
os.chdir(r'C:\Users\tjaber\Desktop\examples')

import pandas as pd
import numpy as np
from sklearn import preprocessing

#reading excel
file1=pd.read_excel('scimagojr-3.xlsx',sheet_name='Sheet1', index_col=0, na_values=['NA'])
file1.head()

file1.loc[[1,2,3,4,5],['Country']]
file1.loc[[5],['Country']]


#writing to excel
df_out = pd.DataFrame([('string1', 1),('string2', 2),('string3', 3)],
                       columns=['Name', 'Value'])
df_out
     
df_out.to_excel('tmp.xlsx')

pd.read_excel('tmp.xlsx')

pd.read_excel('tmp.xlsx', dtype={'Name':str, 'Value':float})

pd.read_excel('tmp.xlsx', na_values=['string1', 'string2'])

#skipping rows with comment
df = pd.DataFrame({'a': ['1', '2', '4'], 'b': ['#2', '#3', '#5']})
df.to_excel('tmp2.xlsx', index=False)
pd.read_excel('tmp2.xlsx')
pd.read_excel('tmp2.xlsx', comment='#')

df = pd.DataFrame({'a': ['#1', '#2', '#4'], 'b': ['2', '3', '5']})
df.to_excel('tmp2.xlsx', index=False)
pd.read_excel('tmp2.xlsx', comment='#')
 
#--------------------------------
#Plotting 

#Matplotlib is the whole package; matplotlib.pyplot is a module in matplotlib; 
#and pylab is a module that gets installed alongside matplotlib.


import matplotlib.pyplot as plt

plt.interactive(False)#interactive mode is off, you have to call plt.show() explicitly to pop up figure window.

x = np.linspace(-2, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.show()
#---------------------------
#Line chart

import matplotlib.pyplot as plt
values = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9]
plt.plot(values)
plt.show()

#Multiple line chart
sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
line_chart1 = plt.plot(range(1,12), sales1)
line_chart2 = plt.plot(range(1,12), sales2)
plt.title('Monthly sales of 2016 and 2017')
plt.xlabel('Sales')
plt.ylabel('Month')
plt.legend(['year 2016', 'year 2017'], loc=1)
plt.show()

#Line style
line_chart1 = plt.plot(range(1,12), sales1,'--')
line_chart2 = plt.plot(range(1,12), sales2,':')

#colour
line_chart1 = plt.plot(range(1,12), sales1,'g')
line_chart2 = plt.plot(range(1,12), sales2,'r')
#-----------------------------

#Pie chart

values = [60, 80, 90, 55, 10, 30]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['US', 'UK', 'India', 'Germany', 'Australia', 'South Korea']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels= values,explode=explode,
        counterclock=False, shadow=True)
plt.title('Population Density Index')
plt.legend(labels,loc=3)
plt.show()

#Percentage
plt.pie(values, colors=colors, labels=labels,
explode=explode, autopct='%1.1f%%', counterclock=True, shadow=True)

#-----------------------------

#Scatter plot chart

weight1=[63.3,57,64.3,63,71,61.8,62.9,65.6,64.8,63.1,68.3,69.7,65.4,66.3,60.7]
height1=[156.3,100.7,114.8,156.3,237.1,123.9,151.8,164.7,105.4,136.1,175.2,137.4,164.2,151,124.3]
 
plt.scatter(weight1,height1,c='b',marker='o')#marker=’o’ denotes the type of plot
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
 
 
weight=np.concatenate((weight1,weight2,weight3))
height=np.concatenate((height1,height2,height3))
len(weight)
len(height)
 
color_array = ['b'] * 15 + ['g'] * 15 + ['r']*15
 
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
plt.xticks(pos, city)
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
plt.bar(pos,Happiness_Index_Female,color='pink',edgecolor='black',bottom=Happiness_Index_Male)
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
 
plt.bar(pos,Happiness_Index_Male,bar_width,color='blue',edgecolor='black')
plt.bar(pos+bar_width,Happiness_Index_Female,bar_width,color='pink',edgecolor='black')
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Group Barchart - Happiness index across cities By Gender',fontsize=18)
plt.legend(Gender,loc=2)
plt.show()

#----------------------------------------------
#Box plot

value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
 
box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data)
plt.show()


#box plot with fills and labels:
bp=plt.boxplot(box_plot_data,patch_artist=True, labels=['course1','course2','course3','course4'])
#argument patch_artist fills the boxplot

for x in bp['boxes']:
    # change outline color
    x.set(color='red', linewidth=2)
    # change fill color
    x.set(facecolor = 'green')
    
    
#Horizontal box with different colors:    
box=plt.boxplot(box_plot_data,vert=0,patch_artist=True,labels=['course1','course2','course3','course4'],)
 
colors = ['cyan', 'lightblue', 'lightgreen', 'tan']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
 
plt.show()    
    

#notch format of the box plot    
plt.boxplot(box_plot_data,notch='True',patch_artist=True,labels=['course1','course2','course3','course4'])    
#----------------------
#Histogram chart
#step type (no fills)
values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,5, histtype='step', align='mid', color='g', label='Test Score Data')
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

df['Name']

x=df['Score'].mean()
type(x)
x
y=np.array(x)
type(y)
y
np.mean(y)



df[['Name', 'Score']]

df[:2]

df['Score'] > 70


df[df['Score'] > 70]

df[(df['Score'] > 70) & (df['Score'] < 85)]

df.ix[:,'Score']

type(df.ix[:,'Score'])
#Indexing with .ix: 

df.ix[3,2]
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


pd.crosstab(df.Subject, df.Result,margins=False)


pd.crosstab([df.Subject, df.Exam],df.Result, margins=True)




































