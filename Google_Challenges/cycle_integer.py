"""
The problem:
Given an integer n in base b, two new values can be created by taking the digits 
of n in ascending and descending order. The difference between these two values 
is used to produce the next n. Find the length of the loop when the values of n 
repeat in a cycle. 

The solution: 
Because any value n will create the same two values when its digits are organized,
once a value n appears again, a cycle is inevitable. The number of values between the 
first n and the first time n reappears (including one of the n's) gives the length of 
the loop.

Create a list that contains all n values and check if it's already in the list when
adding a new n value. 
""" 


def solution(n, b):
	
	id_values = []
		# List of id values that have gone through the algorithm.
		# If the next id is already in the list, we have found
		# our loop starting point

	def chores(n, b):
		# define our algorithm
		
		id_values.append(n)  # add n to id list
		
		k = len(n)	# length of id in base b

		# id values turned to string so digits can be sorted
		pre_y = sorted(n)
		pre_x = pre_y[::-1]

		# x and y turned back to ints, but of base b 
		x = int("".join(pre_x), b)
		y = int("".join(pre_y), b)

		# difference "z" is calculated in base 10
		z = x - y 	

		# z converted to base b
		i = k-1	
		z_b =[]	
		while i >=0:
			exp = b**i 		
			digit = z//exp	
			z_b.append(str(digit))
			z = z - (digit*exp)
			i -= 1
		z = "".join(z_b)

		z = str(z).zfill(k) #leading zeroes added back to z if necessary

		if z in id_values:	
			# if z already in id list, find lenth of loop
			loop_size = (len(id_values) - id_values.index(z))
			return loop_size
		else:
			# recursive call for next id
			return chores(z,b)
		
	return chores(n,b)
