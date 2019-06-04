#!/usr/bin/env python
 
import sys
import string
import numpy

# In this implementation we assume that the  vector can be stored in the memory

#Initializing a empty vector list
v = []

#opens file with name of "input_vector.txt"
f = open('input_vector.txt','r')

while True:
  #Reading lines from input vector file 
  #and appending it to vector v
	line = f.readline()
	line = line.strip()
	if not line:
		break
	else:
		v.append(int(line))
f.close()

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
  #Remove leading and trailing whitespace
  line = line.strip()

  #Split line into array of entry data
  entry = line.split(",")
  row = int(entry[0])
  col = int(entry[1])
  value = int(entry[2])
  temp = v[col]*value #Multiplying Vector Column value
  #with Matrix value of a row but with the same column
  print '%s\t%s' % (row,temp) #printing row and temp