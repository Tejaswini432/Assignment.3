# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:33:32 2020

@author: Tejaswini...!
"""

#to rewrite the pay computation to give the employee 1.5 times the hourly rate of hours worked above 40 hours
hrs = input("Enter hours:")
h = float(hrs)
xx = input("Enter the rate:")
x = float(xx)
if h <= 40 :
     print( h * x)
elif h > 40:
     print(40* x + (h-40)*1.5*x)     

#to rewrite pay program using try and except
try:
    hour = int(input("Enter hour:")) 
    rate = int(input("Enter rate:"))
if hour <= 40;
    print(hour * rate)
elif hour > 40:
    print((hour * rate)+(hour - 40) * (rate * 0.5))
except:
    print("something went wrong,kindly input numeric numbers")

#to prompt a score between 0.0 and 1.0
score = input("Enter score:")
s = float(score)
x = 'error'
if s >= 0.9:
        x = 'A'
elif s >= 0.8:
        x = 'B'
elif s >= 0.7:
        x = 'C'
elif s >= 0.6:
        x = 'D'
elif s < .6:
        x = 'F'
else:
        x = "Out of range" 
print (x)        
    