# Generate Two Random Vectors of any size and save #
#them in a file, which will be an 
#input to Mapreduce Vector Vector Multiplication Task
# Two Vectors are A and B
import numpy as np 

#Randomly Select Size of Vector between 1-10
vector_size = np.random.randint(1,10) 
#Writing Result to input file
with open('input.txt', 'w') as the_file:

	for i in range(vector_size):
		the_file.write('A')
		the_file.write(',')
		the_file.write(str(i))
		the_file.write(',')
		#Writing values of Vector A between 0-10
		the_file.write(str(np.random.randint(0,10)))
		the_file.write('\n')

	for i in range(vector_size):
		the_file.write('B')
		the_file.write(',')
		the_file.write(str(i))
		the_file.write(',')
		#Writing values of Vector B between 0-10
		the_file.write(str(np.random.randint(0,10)))
		the_file.write('\n')

		