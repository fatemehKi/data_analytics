# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:17:32 2019

@author: mfatemeh
"""
import os
import pandas as pd
import numpy as np

os.getcwd()
os.chdir(r'C:\Users\mfatemeh\Desktop\Fatemeh_Kiaie')



#-----------Problem1 
Fraud_Records=pd.read_excel('FraudDetection.xlsx',sheet_name='Sheet1', na_values=['NA'])
Fraud_Records.head()


#-----------Problem 2
X=Fraud_Records.Fraud_Detected

#first method
def target_a(a):
    if a=="Yes":
        return 1
    else:
        return 0


Fraud_Records["Target"]= Fraud_Records[target_a(Fraud_Records.Fraud_Detected)]

Fraud_Records["Target"]=Fraud_Records.Fraud_Detected.apply(target_a) 
       
#second method:
for i in X:
    if Fraud_Records.Fraud_Detected[i]:
        Fraud_Records["Target"]=1
    else:
        Fraud_Records["Target"]=0
      

#third method
Fraud_Records['Target'] = Fraud_Records['X'].astype(int())
Fraud_Records["Target"]= Fraud_Records.Fraud_Detected.apply( np.dtype=int())


del Fraud_Records['X']


#----------- Problem 3
col=Fraud_Records.head(n=0)
list(col)
for i in col:
    print(i)

#--------- Problem 4

pd.crosstab(Fraud_Records.WebsiteRegion, Fraud_Records.Target)

#---------- Problem 5
dt=Fraud_Records.dtypes

for i in col:
    if Fraud_Records[i].dtypes=='object':
        le=len(Fraud_Records[i].unique())
        print(le)
        print(i)
        
#-------- Problem 6
    
q6_1 = Fraud_Records.groupby("WebsiteRegion")["Trans_value"]
me=q6_1.median()

#------ Problem 7

len(Fraud_Records[(Fraud_Records["WebsiteRegion"] == 'US') & (Fraud_Records['Purchase_Category']=='Books')])

#------ Problem 8

Fraud_Records.drop_duplicates(['Transaction_ID'])

#----- Problem 9

def Transaction_Stat(Item_transaction):
    me=Fraud_Records.Item_transaction.mean()
    st=Fraud_Records.Item_transaction.std()
    lst1=[me,st]
    return(lst1)
