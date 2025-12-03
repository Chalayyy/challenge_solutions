"""
The Problem:
Given a natural number (a positive intger), and the option to add 1, 
subtract 1, or divide by 2 if it's even, find the fewest number of steps
required to bring the number to 1.

The Solution:
- Divide by 2 whenever the value is even. (Most efficient option)
- Subtract 1 if the number is 3 or it would make it divisible by 4
(since division is most efficient, and only one of two consecutive 
even numbers can both be divisible by four, shift towards the one that is)
- Add 1 in any other case.

This solution can handle extremely large values (~10,000 digits long)

showsolution() will show the steps taken to go from the number to 1
"""


def solution(n): 
	# Find min steps to go from "n" to 1
	n = int(n)  # n may be given as string, so convert to int
	
	total_steps = 0  # represents how many steps taken so far

	while n != 1:  # 1 is our goal value

		if n%2 == 0:
			# can only divide by two if value is even
			while n%2 == 0:
				# as long as value is even, divide by two and increment steps
				total_steps += 1
				n = n//2

		else:
			# if value isn't even, add or subtract 1
			total_steps += 1
			if (n-1)%4 == 0 or n == 3:
				# Since value is odd, n-1 or n+1 will be even.
				# Dividing by 2 is most effective, so we want
				# a value whose half is also divisible by 2
				# as it is more efficient.
				# Of two consecutive even values only one
				# is divisible by 4, so we shift to that one.
				# (Make exception for 3 since 2 is better than 4)
				n -= 1
			else:
				n +=1

	return total_steps


def showsolution(n):
	# using same algorithm as above to show steps

	n = int(n)
	steps = []
	
	while n != 1:
	
		if n%2 == 0:
			while n%2 == 0:
				steps.append(n)
				n = n//2

		else:
			steps.append(n)
			if n%4 == 0 or n == 3:
				n -= 1
				
			else:
				n += 1
	steps.append(1)
	return steps


# x = "9"*500
# print(solution(x))
# print(showsolution(x))




		

	
