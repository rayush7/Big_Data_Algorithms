#!/usr/bin/env python

#Reducer Code
import sys

#Create an empty ABC dictionaryionary
ABC_dictionary={}

#Create an empty list for key values
key_value_list=[]
 
#For loop to read lines from console
for line in sys.stdin:
	line = line.strip()       #strip out whitespaces
	key_value = line.split('\t')   #split line, into
	# key and value, returns a list
	key_value_list.append(key_value) #Append the 
	#key_value to the key_value_list list

	if key_value[0]=="ABC": #Checking if the zeroth index
	# of the key_value is string ABC
		if ABC_dictionary.has_key(key_value[1])==False:  # Checking if ABC_dictionary
		# has the same key in the first index of key_value
			ABC_dictionary.update({key_value[1]:0}) #updating the value
			# of a key in ABC_dictionary
 
for key_value in key_value_list: #Looping over key_value_list
	if ABC_dictionary.has_key(key_value[0]): #Checking if 
	#ABC_dictionary has a key stored on zero index of key_value
		ABC_dictionary[key_value[0]]+=int(key_value[1]) #Incrementing the value
		# corresponding to a key in ABC Dictionary
#Prnting the value of the ABC_dictionary
for key, value in ABC_dictionary.iteritems():
	print( '%s %s' % (key, value))