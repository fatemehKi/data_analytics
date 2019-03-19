# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:08:59 2019

@author: mfatemeh
"""

'''
- with the properties we don't have the () but with the methods we do have the parantesis and can have args
- the properties giving a component or individual elements of an object we use '.' of the object
- the built date and time function for the current date are the datetime.today() and datetime.now()
- in order to replace a part in the object
- in the replace method if we don't mention the argument that we want to change the first argumern  will change only
- the date object is in the date package then we can use the date.
- if the package was imported once in the session and if we erase it will be still effected. you have to run spyder again to have it effected
- we can return a timedelta type data using day1-day2
- if an argument (year, month,..) in the datetime has not beed defined, it is assumed to be zero
'''
from datetime import datetime, date, time, timedelta
datetime.today()

dt=datetime(2013, 5, 17, 16, 21, 18) #the following are the properties
dt.year
dt.month
dt.microsecond


new_dt=dt.replace(minute=10, second=0) # the dt doesn't change.. implace update feature is false
new_dt.second
new_dt.minute
dt.second
dt.minute

new_dt2=dt.replace(10)

d= date(2014, 11, 18) # d is the object and to change it to string we use str
str(d)

date.today() #make sure the date package has been imported

d1=date(2013, 5, 17)
d2=date(2013, 5, 12)
d1-d2 #the output is datetime.timedelta(5); it shows the day adn 

dt1=datetime(2014, 12, 11, 10, 22)
dt2=datetime(2014, 12, 11, 9, 22)
dt1-dt2 #the output is datetime.timedelta(0, 3600)


# Add a timedelta
delta=timedelta(hours=72, minutes=0, seconds=0)
dt=datetime(2014, 10, 10, 12, 25)
print(dt+delta)

          
