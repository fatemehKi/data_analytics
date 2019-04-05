# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:31:00 2019

@author: mfatemeh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:16:05 2019

@author: Kian
"""

import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# getting the data fro the directory and assigning an object to the data frame
os.chdir(r'C:\Users\mfatemeh\Desktop\python')
emp_comp=pd.read_csv('Employee_Compensation.csv')

# a subset of te data is rndomly selected (in rder to avoi loosing the randomness of data)
empc_sub = emp_comp.sample(n=10000)


#######----------------------------data cleaning--------------------------#######
# 1.droping duplicates
empc_sub[empc_sub.duplicated()==True].shape 
#the result showing there is no duplicated row however, since the input is random, we leave the code below to remove the duplicated
empcs_nodu = empc_sub.drop_duplicates()

# 2. dropping records with the invalid (negative) data in salary+benefits (compensation)
empcsn_cl1= empcs_nodu[(empcs_nodu['Salaries'] >=0) & (empcs_nodu['Overtime'] >=0) & (empcs_nodu['Other Salaries'] >=0) & (empcs_nodu['Total Salary'] >=0) & \
                       (empcs_nodu['Retirement'] >=0) & (empcs_nodu['Health and Dental'] >=0) & (empcs_nodu['Other Benefits'] >=0) & (empcs_nodu['Total Benefits'] >=0) & \
                       (empcs_nodu['Total Compensation'] >=0)]

# 3. removing records with the invalid year (future or too old)
empcsn_cl2= empcsn_cl1[(empcsn_cl1['Year'] >=2000) & (empcsn_cl1['Year'] < 2019)]
 
#4. removing the rows with the 75 % of missing data for the salary info columns or compensation column
empcsn_cl3= empcsn_cl2[(empcs_nodu['Salaries'] ==0) & (empcs_nodu['Overtime'] ==0) & (empcs_nodu['Other Salaries'] ==0) & (empcs_nodu['Total Salary'] ==0) & \
                       (empcs_nodu['Retirement'] ==0) & (empcs_nodu['Health and Dental'] ==0) & (empcs_nodu['Other Benefits'] ==0) & (empcs_nodu['Total Benefits'] ==0) & \
                       (empcs_nodu['Total Compensation'] ==0)]
empcsn_cl4= pd.concat([empcsn_cl2, empcsn_cl3, empcsn_cl3]).drop_duplicates(keep=False)

# data frame been reindexed to start from 0
df_cleaned=empcsn_cl4.reset_index(drop=True)
df_cleaned.head(5)
#######----------------------------data analysis--------------------------#######
####Q1: (a) Specifying the classification of the (1) Organization Group (2) Department Code (3) Department,
# (4) Union (5) Job Family (6) Job  (b) Specifying the population in each class

Q1a_OG=df_cleaned['Organization Group'].unique()
Q1b_OG=df_cleaned['Organization Group'].value_counts()
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'w']
plt.pie(Q1b_OG, colors=colors, labels=Q1a_OG, autopct='%1.2f%%', counterclock=False, shadow=True)

plt.show() 



city=['Delhi','Beijing','Washington','Tokyo','Moscow']
pos = np.arange(len(Q1b_OG))
 
'''plt.bar(pos,Q1b_OG,color='blue',edgecolor='black')
plt.xticks(pos, Q1a_OG) #xtick uses the city for the pos.. without the xtick we will see 0,1,2,..
plt.xlabel(' ', fontsize=5)
plt.ylabel(' ', fontsize=16)
plt.title('Barchart - Happiness index across cities',fontsize=20)
plt.show()'''


Q1a_DC=df_cleaned['Department Code'].unique()
Q1b_DC=df_cleaned['Department Code'].value_counts()

Q1a_D=df_cleaned['Department'].unique()
Q1b_D=df_cleaned['Department'].value_counts()

Q1a_U=df_cleaned['Union'].unique()
Q1b_U=df_cleaned['Union'].value_counts() 

Q1a_JF=df_cleaned['Job Family'].unique()
Q1b_JF=df_cleaned['Job Family'].value_counts()

values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,bins=5, histtype='step', align='mid', color='g', label='Test Score Data') #5 is the number of bins the number of the steps is bins-1
plt.legend(loc=2)
plt.title('Histogram of score')
plt.show()



Q1a_J=df_cleaned['Job'].unique()
Q1b_J=df_cleaned['Job'].value_counts()



################################Fatemeh showing in the pie chart or abr chart

####Q2: Specifiyg the year, organization group, department code, department, union, job family and the job with
# the maximum salary, maximum benefit, maximum compensation as well as minimum salary, minimum benefit,
# minimum compensation and also the mean value for salary, benefit and compensation
MAX_TSalary=df_cleaned[df_cleaned['Total Salary']==df_cleaned['Total Salary'].max()]
MAX_TBenefits=df_cleaned[df_cleaned['Total Benefits']==df_cleaned['Total Benefits'].max()]
MAX_TCompensation=df_cleaned[df_cleaned['Total Compensation']==df_cleaned['Total Compensation'].max()]

#--to find the minimum we need to remove the rows with the zero salary and then apply the zero
df_cleaned_minTSalary= df_cleaned[df_cleaned['Total Salary'] !=0]
MIN_TSalary=df_cleaned_minTSalary[df_cleaned_minTSalary['Total Salary']==df_cleaned_minTSalary['Total Salary'].min()]

df_cleaned_minTBenefits= df_cleaned[df_cleaned['Total Benefits'] !=0]
MIN_TBenefits=df_cleaned_minTBenefits[df_cleaned_minTBenefits['Total Benefits']==df_cleaned_minTBenefits['Total Benefits'].min()]

df_cleaned_minTCompensation= df_cleaned[df_cleaned['Total Compensation'] !=0]
MIN_TCompensation=df_cleaned_minTCompensation[df_cleaned_minTCompensation['Total Compensation']==df_cleaned_minTCompensation['Total Compensation'].min()]


AVG_TSalary=df_cleaned['Total Salary'].mean()
AVG_TBenefits=df_cleaned['Total Benefits'].mean()
AVG_TCompensation=df_cleaned['Total Compensation'].mean()


####Q3: (a)Specify the average total salary and total compensation for each organization group and 
#(b) Specify the average total salary adn total compensation for each organization group in each year

#A(a) mean of total salary in each group
TSalary_inOG = df_cleaned.groupby("Organization Group")["Total Salary"]
TSalary_inOG.mean()
#mean of total compensation in each group
TCompens_inOG = df_cleaned.groupby("Organization Group")["Total Compensation"]
TCompens_inOG.mean()

#A(b) mean of total salary in each group per year
year_TSalary_inOG=df_cleaned.pivot_table(index='Year', values='Total Salary', columns= 'Organization Group', aggfunc=np.mean)
#mean of total compensation in each group per year
year_TCompens_inOG=df_cleaned.pivot_table(index='Year', values='Total Compensation', columns= 'Organization Group', aggfunc=np.mean)


#### Q4: Specify the list with minimum numer of job code that has the 25% of the sumation of total compenastion 
threshold=(df_cleaned['Total Compensation'].sum())*0.25
s_df=df_cleaned.sort_values(['Total Compensation'], ascending= False)

sum_comp=0
li=[]
for  index, row in s_df.iterrows():
    sum_comp= sum_comp+row['Total Compensation']
    #print(row['Total Compensation'])
    if (sum_comp< threshold):
        li.append(row['Total Compensation'])
    
len(li)  #shows the number of job codes that will coce

