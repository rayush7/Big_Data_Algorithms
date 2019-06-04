#!/usr/bin/env python
import sys

prev_word = " "
months = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Nov','Dec']
dates_to_output = [] #an empty list to hold dates for a given word

day_cnts_to_output = [] #an empty list of day counts for a given word

line_cnt = 0

#count input lines
for line in sys.stdin:
	line = line.strip()
	key_value = line.split('\t')
	line_cnt = line_cnt+1
	curr_word = key_value[0]
	value_in = key_value[1]

	if curr_word != prev_word:
	# -----------------------
	#now write out the join result, but not for the first line input
	# -----------------------
		if line_cnt>1:
			for i in range(len(dates_to_output)): #loop thru dates, indexes start at 0
				print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))
		#now reset lists
			dates_to_output=[]
			day_cnts_to_output=[]

		prev_word=curr_word #set up previous word for the next set of input lines


	if (value_in[0:3] in months):
		date_day =value_in.split() #split the value field into a date and day-cnt
		#add date to lists of the value fields we are building	
		dates_to_output.append(date_day[0])
		day_cnts_to_output.append(date_day[1])
	else:
		curr_word_total_cnt = value_in #if the value field was just the total count then its
		
for i in range(len(dates_to_output)): #loop thru dates, indexes start at 0
	print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))