#!/usr/bin/env python

import sys
import string
import numpy

#Initialising the Variables
last_key=""
product=1
count=0
total = 0

for line in sys.stdin:


  line = line.strip() #removing whitespaces
    

  key, value = line.split('\t',1)
  #Checking if last is empty and current key is 
  #not equal to last key

  if last_key != "" and key != last_key:
    if count==2:
      #print '%s\t%s' % (last_key,product)
      #Accumulating the Sum
      total=total+int(product)

    product = int(value) #typecasting value into integer
    last_key = key #Setting last key to current key
    count = 1 

  else:
    product = product*int(value)#Multiplying prervious product value with value
    last_key=key #Set last key equal to current key
    count=count+1

#the last key
if count==2:
  #print '%s\t%s' % (last_key,product)
  total = total + int(product)

print total