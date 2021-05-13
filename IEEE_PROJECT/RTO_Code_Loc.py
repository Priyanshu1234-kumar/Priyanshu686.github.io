# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:50:37 2021

@author: priyanshu kumar
"""
#PROGRAM TO SHOW RTO LOCATION WITH RTO CODE OF TAMILNADU AND BIHAR
import csv
def RTO_CODE():
    Code=input('Enter RTO Code:')
    file=open('RTO_CODE.CSV','r')
    Read_Code=csv.reader(file)
    for row in Read_Code:
        if Code in row[1]:
            print(row)
            
def RTO_LOC():
    Loc=input('Enter RTO Loc:')
    file=open('RTO_CODE.CSV','r')
    Read_Loc=csv.reader(file)
    for row in Read_Loc:
        if Loc in row[0]:
            print(row)
            
print('Enter 1 to search with RTO CODE')
print('Enter 2 to search with RTO LOC')

Value=int(input('Enter here:'))
if Value==1:
    RTO_CODE()
elif Value==2:
    RTO_LOC()
else:
    print('invalid input')
    
while True:
    user_choice = input("Do you want to enter again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        Value=int(input('Enter here:'))
        if Value==1:
           RTO_CODE()
        elif Value==2:
           RTO_LOC()
        else:
           print('invalid input')
        
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break

