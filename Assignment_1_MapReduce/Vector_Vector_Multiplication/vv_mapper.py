#!/usr/bin/env python
 
import sys
import string
import numpy

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
  #Remove leading and trailing whitespace
  line = line.strip()

  #Split line into array of entry data
  entry = line.split(",")
  index = entry[1] #Storing the index
  number = entry[2] #Storing the value

  print '%s\t%s' % (index,number)