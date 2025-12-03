"""
The Problem:
Given a natural number (a positive intger), and the option to add 1, 
subtract 1, or divide by 2 if it's even, find the fewest number of steps
required to bring the number to 1.

The Solution:
- Divide by 2 whenever the value is even. (Most efficient option)
- Use recursion to find whether adding 1 or subtracting 1 is more efficient.

showsolution() will show the steps taken to go from the value to 1

Can handle large values (~13 digits long for solution, ~9 digits long for showsolution). 
"""


def solution(n): 
	# Find min steps to go from "n" to 1
	n = int(n)  # n may be given as string, so convert to int
	
	total_steps = 0  # represents how many steps taken so far
	
	if n == 1:
		# recursion base case
		return total_steps
	
	elif n%2 == 0:
		# if n is even, keep dividing until not even
		# since it is the best option
		while n%2 == 0:
			total_steps += 1
			n = n//2
		return total_steps + solution(n)


	else:
		# use recursion to find best solution
		total_steps += 1
		return total_steps + min(solution(n+1), solution(n-1))


def showsolution(n):
	# using same algorithm as above to show steps

	n = int(n)
	steps = []
	
	if n == 1:
		steps.append(1)
		return steps
	
	elif n%2 == 0:
		while n%2 == 0:
			steps.append(n)
			n = n//2	
		steps.extend(showsolution(n))
		return steps

	else:
		steps.append(n)
		if len(showsolution(n-1)) <= len(showsolution(n+1)):
			steps.extend(showsolution(n-1))
			return steps
		else:
			steps.extend(showsolution(n+1))
			return steps


# x = 999
# print(solution(x))
# print(showsolution(x))
