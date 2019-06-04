# Generate Two Random Vectors of any size and save them in a 
#file, which will be an input to Mapreduce 
#Vector Vector Multiplication Task

# Two Vectors are A and B
import numpy as np 

#Randomly Choosing the Matrix Row Size between 2-10
matrix_row = np.random.randint(2,10)
#Randomly Choosing the Matrix Column Size between 2-10
matrix_col = np.random.randint(2,10)
#Matrix Col will be equal to Vector Size
vector_size = matrix_col

# Code to Generate the Vector and write it to a file
with open('input_vector.txt', 'w') as the_file:

	for i in range(vector_size):
		#the_file.write(str(i))
		#the_file.write(',')
		#Randomly Selecting Vector Values between 0-10
		the_file.write(str(np.random.randint(0,10)))
		the_file.write('\n')

# Code to Generate the Matrix and write it to a file
M = np.matrix(np.random.randint(0,10, size=(matrix_row, matrix_col)))

#Writing Matrix into Input_Matrix.txt file
with open('input_matrix.txt', 'w') as the_file:
	for (i,j), value in np.ndenumerate(M):
		if value==0:
			continue
		else:
			the_file.write(str(i))
			the_file.write(',')
			the_file.write(str(j))
			the_file.write(',')
			the_file.write(str(value))
			the_file.write('\n')
		