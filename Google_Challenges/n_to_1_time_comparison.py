"""
This function compares the time to execute two codes for 
determining the shortest number of steps to get from any natural 
number (positive whole number) to 1 by only dividing by 2, adding 1, 
or subtracting 1. 

solution1() is generally faster for terms with more than ~38 digits.
solution2() is generally faster for terms with less than ~38 digits.

Includes edits for python2.7 vs 3
"""

from time import process_time_ns  # python3
# import timeit  f# python2.7

def solution1(n): 
	
	n = int(n)
	
	total_steps = 0

	while n != 1:

		if n%2 == 0:
			while n%2 == 0:
				total_steps += 1
				n = n//2

		else:
			total_steps += 1
			if (n-1)%4 == 0 or n == 3:
				n -= 1
			
			else:
				n +=1

	return total_steps


def solution2(n): 

	n = int(n)
	
	def solution3(n):
		total_steps = 0

		if n == 1:
			return total_steps
		
		if n%2 == 0:
			# if n is even, keep dividing until not even
			while n%2 == 0:
				total_steps += 1
				n = n//2
			return total_steps + solution3(n)


		else:
			# add or subtract 1 depending on which is divisible by 4
			total_steps += 1
			
			if (n-1)%4 == 0 or n == 3:
				return total_steps + solution3(n-1)
			
			else:
				return total_steps + solution3(n+1)

	return solution3(n)


# python3
# x = "9"*38
# start1 = process_time_ns()
# print(solution1(x))
# end1 = process_time_ns()
# print(f"Time1: {end1-start1}")

# start2 = process_time_ns()
# print(solution2(x))
# end2 = process_time_ns()
# print(f"Time2: {end2-start2}")

# python2.7
# start = timeit.default_timer()
# print(solution1(x))
# diff = timeit.default_timer() - start
# print(diff)

# start = timeit.default_timer()
# print(solution2(x))
# diff = timeit.default_timer() - start
# print(diff)



