#!/usr/bin/env python
import sys


for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",") #split line, into key 
    #and value, returns a list
    key_in     = key_value[0].split(" ")   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    #print key_in
    if len(key_in)>=2: #if this entry has <date word> in key
        date = key_in[0] #now get date from key field
        word = key_in[1]
        value_out = date+" "+value_in #concatenate date
        #, blank, and value_in
        print( '%s\t%s' % (word, value_out) )  #print a string, tab, and string
    else:   #key is only <word> so just pass it through
        print( '%s\t%s' % (key_in[0], value_in) )  #print a string tab and string