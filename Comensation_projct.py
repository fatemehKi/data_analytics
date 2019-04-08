"""
/********************************************************************
 * @file Project.py 
 * @The goal of the project is to analyse the compensation data set
 * @author Fatemeh Kiaie
 * @Contact: f.kiaie@gmail.com
 ***********************************************************************/
"""
""""
Questions to respond:
    Q1. 
    - (a) Specifying Number of groups in different classification criteria for
    the input columns:
    (1) Organization Group (2) Department Code (3) Department, (4) Union 
    (5) Job Family (6) Job  
    - (b) Specifying the population in each classification
    
    Q2. 
    Specifiyg the year, organization group, department code, department,
    union, job family and the job with the maximum salary, maximum benefit,
    maximum compensation as well as minimum salary, minimum benefit, minimum 
    compensation and also the mean value for salary, benefit and compensation    
    
   Q3. 
   - (a) Specify the average total salary, average total compensation, and 
   average total benefits for each organization group
   - (b) Specify the average total salary and total compensation for each 
    organization group in each year
    
   Q4.
   Specifying the summation of spending in overtime for each group

   Q5.
   Specify the sub_set with minimum numer of job code that has the 25% of the
   sumation of total compenastion

   Q7.
   Specify the percentage of the jobs that have the retirment plan
   
""""

#######----------------------------Inclusing packages---------------------#######
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# getting the data fro the directory and assigning an object to the data frame
os.chdir(r'C:\Users\Kiaie\Desktop\project_python')
emp_comp=pd.read_csv('Employee_Compensation.csv')

# a subset of te data is rndomly selected (in order to avoid loosing the randomness of data)
empc_sub = emp_comp.sample(n=10000)
empc_sub.to_excel('tmp2.xlsx')

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
 
#4. removing the rows with the of missing data for the output columns
empcsn_cl3= empcsn_cl2[(empcs_nodu['Salaries'] ==0) & (empcs_nodu['Overtime'] ==0) & (empcs_nodu['Other Salaries'] ==0) & (empcs_nodu['Total Salary'] ==0) & \
                       (empcs_nodu['Retirement'] ==0) & (empcs_nodu['Health and Dental'] ==0) & (empcs_nodu['Other Benefits'] ==0) & (empcs_nodu['Total Benefits'] ==0) & \
                       (empcs_nodu['Total Compensation'] ==0)]

empcsn_cl4= pd.concat([empcsn_cl2, empcsn_cl3, empcsn_cl3]).drop_duplicates(keep=False)

# data frame been reindexed to start from 0
df_cleaned=empcsn_cl4.reset_index(drop=True)

#######----------------------------data analysis--------------------------#######
####Q1. - (a) Specifying Number of groups in different classification criteria 
#for the input columns: (1) Organization Group (2) Department Code (3) Department,
#(4) Union  (5) Job Family (6) Job  
#       - (b) Specifying the population in each classification

Q1a_OG=df_cleaned['Organization Group'].unique()
Q1b_OG=df_cleaned['Organization Group'].value_counts()
len(Q1a_OG)

Q1a_DC=df_cleaned['Department Code'].unique()
Q1b_DC=df_cleaned['Department Code'].value_counts()
len(Q1a_DC)

Q1a_D=df_cleaned['Department'].unique()
Q1b_D=df_cleaned['Department'].value_counts()
len(Q1a_D)

Q1a_U=df_cleaned['Union'].unique()
Q1b_U=df_cleaned['Union'].value_counts()
len(Q1a_U)

Q1a_JF=df_cleaned['Job Family'].unique()
Q1b_JF=df_cleaned['Job Family'].value_counts()
len(Q1a_JF)

Q1a_J=df_cleaned['Job'].unique()
Q1b_J=df_cleaned['Job'].value_counts()
len(Q1a_J)


Catg=['Org Group','Dep. Code', 'Department', 'Union','Job Family', 'Job']
pos = np.arange(len(Catg))
Dist=[len(Q1a_OG), len(Q1a_DC), len(Q1a_D), len(Q1a_U), len(Q1a_JF), len(Q1a_J)]


mpl.rcParams['font.size'] = 9.0
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size

plt.bar(pos,Dist,color='c',edgecolor='black')
plt.xticks(pos, Catg) #xtick uses the city for the pos.. without the xtick we will see 0,1,2,..
plt.xlabel('Type of Classification', fontsize=15)
plt.ylabel('Number of Groups', fontsize=15)
plt.title('Demographic distribution of jobs based on differnt classification',fontsize=20)
plt.show()

mpl.rcParams['font.size'] = 18
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'w']
plt.pie(Q1b_OG, colors=colors, labels=Q1a_OG, autopct='%1.2f%%', counterclock=False, shadow=True)
plt.show() 


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

box_plot_data=[df_cleaned['Total Salary'], df_cleaned['Total Benefits'],df_cleaned['Total Compensation']]
bp=plt.boxplot(box_plot_data,patch_artist=True, labels=['Total Salary','Total Benefits','Total Compensation']) #to fill the box with the default colour

for x in bp['boxes']: #the Box inside the bp is the reserved key word for the 
    # change outline color
    x.set(color='black', linewidth=2) #this refers to the color of the outliner
    x.set(facecolor = 'green') 
    
plt.show()

####Q3: (a)Specify the average total salary, average total compensation, and average total benefits for each organization group and 
#(b) Specify the average total salary adn total compensation for each organization group in each year

#A(a) mean of total salary in each group
TSalary_inOG = df_cleaned.groupby("Organization Group")["Total Salary"]
TSalary_inOG.mean()

Cm_h= df_cleaned[df_cleaned['Organization Group']=='Community Health']["Total Salary"]
C_r= df_cleaned[df_cleaned['Organization Group']=='Culture & Recreation']["Total Salary"]
G_a_f=df_cleaned[df_cleaned['Organization Group']=='General Administration & Finance']["Total Salary"]
G_c_r=df_cleaned[df_cleaned['Organization Group']=='General City Responsibilities']["Total Salary"]
H_w_n_d=df_cleaned[df_cleaned['Organization Group']=='Human Welfare & Neighborhood Development']["Total Salary"]
P_p=df_cleaned[df_cleaned['Organization Group']=='Public Protection']["Total Salary"]
P_w=df_cleaned[df_cleaned['Organization Group']=='Public Works, Transportation & Commerce']["Total Salary"]

mpl.rcParams['font.size'] = 18
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
bp2=plt.boxplot([Cm_h, C_r, G_a_f, G_c_r, H_w_n_d, P_p, P_w], vert=0, patch_artist=True, labels=['Community Health','Culture & Recreation','General Administration & Finance', 'General City Responsibilities', 'Human Welfare & Neighborhood Development', 'Public Protection', 'Public Works, Transportation & Commerce' ])
for x in bp2['boxes']: #the Box inside the bp is the reserved key word for the 
    # change outline color
    x.set(color='black', linewidth=2) #this refers to the color of the outliner
    x.set(facecolor = 'b') 
plt.show()

#mean of total compensation in each group
TCompens_inOG = df_cleaned.groupby("Organization Group")["Total Compensation"]
TCompens_inOG.mean()

CCm_h= df_cleaned[df_cleaned['Organization Group']=='Community Health']["Total Compensation"]
CC_r= df_cleaned[df_cleaned['Organization Group']=='Culture & Recreation']["Total Compensation"]
CG_a_f=df_cleaned[df_cleaned['Organization Group']=='General Administration & Finance']["Total Compensation"]
CG_c_r=df_cleaned[df_cleaned['Organization Group']=='General City Responsibilities']["Total Compensation"]
CH_w_n_d=df_cleaned[df_cleaned['Organization Group']=='Human Welfare & Neighborhood Development']["Total Compensation"]
CP_p=df_cleaned[df_cleaned['Organization Group']=='Public Protection']["Total Compensation"]
CP_w=df_cleaned[df_cleaned['Organization Group']=='Public Works, Transportation & Commerce']["Total Compensation"]

mpl.rcParams['font.size'] = 18
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
bp3=plt.boxplot([CCm_h, CC_r, CG_a_f, CG_c_r, CH_w_n_d, CP_p, CP_w], vert=0, patch_artist=True, labels=['Community Health','Culture & Recreation','General Administration & Finance', 'General City Responsibilities', 'Human Welfare & Neighborhood Development', 'Public Protection', 'Public Works, Transportation & Commerce' ]) #to fill the box with the default colour
for y in bp3['boxes']: #the Box inside the bp is the reserved key word for the 
    # change outline color
    y.set(color='black', linewidth=2) #this refers to the color of the outliner
    y.set(facecolor = 'r') 
plt.show()

#mean of total benefits in each group
TCompens_inOG = df_cleaned.groupby("Organization Group")["Total Benefits"]
TCompens_inOG.mean()

BCm_h= df_cleaned[df_cleaned['Organization Group']=='Community Health']["Total Benefits"]
BC_r= df_cleaned[df_cleaned['Organization Group']=='Culture & Recreation']["Total Benefits"]
BG_a_f=df_cleaned[df_cleaned['Organization Group']=='General Administration & Finance']["Total Benefits"]
BG_c_r=df_cleaned[df_cleaned['Organization Group']=='General City Responsibilities']["Total Benefits"]
BH_w_n_d=df_cleaned[df_cleaned['Organization Group']=='Human Welfare & Neighborhood Development']["Total Benefits"]
BP_p=df_cleaned[df_cleaned['Organization Group']=='Public Protection']["Total Benefits"]
BP_w=df_cleaned[df_cleaned['Organization Group']=='Public Works, Transportation & Commerce']["Total Benefits"]

mpl.rcParams['font.size'] = 18
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
bp4=plt.boxplot([CCm_h, CC_r, CG_a_f, CG_c_r, CH_w_n_d, CP_p, CP_w], vert=0, patch_artist=True, labels=['Community Health','Culture & Recreation','General Administration & Finance', 'General City Responsibilities', 'Human Welfare & Neighborhood Development', 'Public Protection', 'Public Works, Transportation & Commerce' ]) #to fill the box with the default colour
for y in bp4['boxes']: #the Box inside the bp is the reserved key word for the 
    # change outline color
    y.set(color='black', linewidth=2) #this refers to the color of the outliner
    y.set(facecolor = 'm') 
plt.show()


#A(b) mean of total salary in each group per year
year_TSalary_inOG=df_cleaned.pivot_table(index='Year', values='Total Salary', columns= 'Organization Group', aggfunc=np.mean)

line_chart1 = plt.plot(year_TSalary_inOG.index, year_TSalary_inOG['Community Health'] , color='r', linestyle='-')
line_chart2 = plt.plot(year_TSalary_inOG.index, year_TSalary_inOG['Culture & Recreation'] , color='g', linestyle=':')
line_chart3 = plt.plot(year_TSalary_inOG.index, year_TSalary_inOG['General Administration & Finance'] , color='b', linestyle='-.')
line_chart4 = plt.plot(year_TSalary_inOG.index, year_TSalary_inOG['General City Responsibilities'] , color='c')
line_chart5 = plt.plot(year_TSalary_inOG.index, year_TSalary_inOG['Human Welfare & Neighborhood Development'] , color='m', linestyle='-')
line_chart6 = plt.plot(year_TSalary_inOG.index, year_TSalary_inOG['Public Protection'] , color='k', linestyle=':')
line_chart7 = plt.plot(year_TSalary_inOG.index, year_TSalary_inOG['Public Works, Transportation & Commerce'] , color='y')
plt.title('Average Salary of Each Organization During the Last 5 Years')
plt.ylabel('Average Salary')
plt.xlabel('Year')
plt.legend(['Community Health', 'Culture & Recreation', 'General Administration & Finance', 'General City Responsibilities', 'Human Welfare & Neighborhood Development', 'Public Protection', 'Public Works, Transportation & Commerce' ], loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=2, prop={'size': 14})
plt.show()


#mean of total compensation in each group per year
year_TCompens_inOG=df_cleaned.pivot_table(index='Year', values='Total Compensation', columns= 'Organization Group', aggfunc=np.mean)

line_chart11 = plt.plot(year_TCompens_inOG.index, year_TCompens_inOG['Community Health'] , color='r', linestyle='-')
line_chart12 = plt.plot(year_TCompens_inOG.index, year_TCompens_inOG['Culture & Recreation'] , color='g', linestyle=':')
line_chart13 = plt.plot(year_TCompens_inOG.index, year_TCompens_inOG['General Administration & Finance'] , color='b', linestyle='-.')
line_chart14 = plt.plot(year_TCompens_inOG.index, year_TCompens_inOG['General City Responsibilities'] , color='c')
line_chart15 = plt.plot(year_TCompens_inOG.index, year_TCompens_inOG['Human Welfare & Neighborhood Development'] , color='m', linestyle='-')
line_chart16 = plt.plot(year_TCompens_inOG.index, year_TCompens_inOG['Public Protection'] , color='k', linestyle=':')
line_chart17 = plt.plot(year_TCompens_inOG.index, year_TCompens_inOG['Public Works, Transportation & Commerce'] , color='y')
plt.title('Average Compensation of Each Organization During the Last 5 Years')
plt.ylabel('Average Compensation')
plt.xlabel('Year')
plt.legend(['Community Health', 'Culture & Recreation', 'General Administration & Finance', 'General City Responsibilities', 'Human Welfare & Neighborhood Development', 'Public Protection', 'Public Works, Transportation & Commerce' ], loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=2, prop={'size': 14})
plt.show()


#mean of total benefit in each group per year
year_TBenefi_inOG=df_cleaned.pivot_table(index='Year', values='Total Benefits', columns= 'Organization Group', aggfunc=np.mean)

line_chart21 = plt.plot(year_TBenefi_inOG.index, year_TBenefi_inOG['Community Health'] , color='r', linestyle='-')
line_chart22 = plt.plot(year_TBenefi_inOG.index, year_TBenefi_inOG['Culture & Recreation'] , color='g', linestyle=':')
line_chart23 = plt.plot(year_TBenefi_inOG.index, year_TBenefi_inOG['General Administration & Finance'] , color='b', linestyle='-.')
line_chart24 = plt.plot(year_TBenefi_inOG.index, year_TBenefi_inOG['General City Responsibilities'] , color='c')
line_chart25 = plt.plot(year_TBenefi_inOG.index, year_TBenefi_inOG['Human Welfare & Neighborhood Development'] , color='m', linestyle='-')
line_chart26 = plt.plot(year_TBenefi_inOG.index, year_TBenefi_inOG['Public Protection'] , color='k', linestyle=':')
line_chart27 = plt.plot(year_TBenefi_inOG.index, year_TBenefi_inOG['Public Works, Transportation & Commerce'] , color='y')
plt.title('Average Benefits of Each Organization During the Last 5 Years')
plt.ylabel('Average Benefits')
plt.xlabel('Year')
plt.legend(['Community Health', 'Culture & Recreation', 'General Administration & Finance', 'General City Responsibilities', 'Human Welfare & Neighborhood Development', 'Public Protection', 'Public Works, Transportation & Commerce' ], loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=2, prop={'size': 14})
plt.show()

#### Q4: Specifying the summation of overtime for each group
Sovertime_inOG = df_cleaned.groupby("Organization Group")["Overtime"]
su=Sovertime_inOG.sum()

Categ=['Community Health','Culture & Recreation','General Administration & Finance', 'General City Responsibilities', 'Human Welfare & Neighborhood Development', 'Public Protection', 'Public Works, Transportation & Commerce' ]
pos = np.arange(len(Categ))
 
plt.barh(pos,su,color='blue',edgecolor='black')
plt.yticks(pos, Categ) 
plt.xlabel('Amount of Overtime', fontsize=16)
plt.title('Overtieme of Each Organization',fontsize=20)
plt.show()

#### Q5: Specify the sub_set with minimum numer of job code that has the 25% of the sumation of total compenastion
threshold=(df_cleaned['Total Compensation'].sum())*0.25
s_df=df_cleaned.sort_values(['Total Compensation'], ascending= False)


sum_comp=0
li=[]
for  index, row in s_df.iterrows():
    sum_comp= sum_comp+row['Total Compensation']
    #print(row['Total Compensation'])
    if (sum_comp< threshold):
        li.append(row['Total Compensation'])
    
len(li) 

#### Q6: Specify the percentage of health and dental over the total benefit
n=df_cleaned['Health and Dental'].mean()
d=df_cleaned['Total Benefits'].mean()
n/d

#### Q7: Specify the percentage of the jobs that have the retirment plan
n2=len(df_cleaned[(df_cleaned['Retirement'] !=0) & (df_cleaned['Total Salary'] !=0)])
n2/10000 #number of symbols   
    

