#!/usr/bin/env python

# Mapper Code
import sys

for line in sys.stdin:
    print line
    line = line.strip()   #strip out carriage return
    key_value = line.split(",")   #split line, into key and value, returns a list
    key_in = key_value[0]#.split(" ")   #key is first item in list
    value_in = key_value[1]   #value is 2nd item 
    test_Num=[int(x) for x in value_in.split() if x.isdigit()] #Loop over value_
    #in elements #and check if they are digits
    
    if len(test_Num)>0: #Checking if the size of list
    # test_Num is greater than zero
        print( '%s\t%s' % (key_in, value_in))
    else:
        if value_in == 'ABC': #Checking if the value_in is equal to ABC
            print( '%s\t%s' % ( value_in, key_in))

