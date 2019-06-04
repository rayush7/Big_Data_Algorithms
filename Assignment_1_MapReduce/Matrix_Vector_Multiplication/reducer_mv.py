#!/usr/bin/env python

import sys
import string
import numpy

#Initialization of the Value
current_key = None
current_value = 0
key = None

#Looping over values on Standard Output
for line in sys.stdin:
    line = line.strip() #Remove Whitespaces
    key, value = line.split('\t',1)

    # Convert the value from string into Integer 
    #Introducing Exception Handling
    try:
        value = int(value)
    except ValueError:
        continue

    # if the current key is equal to key
    if current_key == key:
        current_value += value # Incrementing Current Value by Value
    else:
        if current_key:
        # Printing the current key and current value
            print '%s\t%s' % (current_key, current_value)
        current_value = value #Set current_value to value
        current_key = key #Set current_key to key

# Printing Last Value
if current_key == key:
    print '%s\t%s' % (current_key, current_value)