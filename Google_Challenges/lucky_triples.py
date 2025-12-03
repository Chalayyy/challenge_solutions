"""
The problem: 
This code is designed to take a list (size 2-2000) of positive integers l (values 1-999999)
and counts the number of "lucky triples" (li, lj, lk) where li is a factor of lj which is a factor of lk 
where the list indices meet the requirement i < j < k. 

The solution:
For each value in the list, we find which (and how many) previous values are a factor of that value. 
The number of lucly triples is the sum of the number of factors each factor has.

For example, suppose we have the list [1,2,4,5,6,7,11,12] and we are on the value 12, which has the previous
values 1,2,4,6 as factors. We add the number of previous value factors that 1,2,4,6 each have (0+1+2+2 = 5) 
to our lucky triple count. This is because if 4 is a factor of 12, then any factor of 4 will create a lucky triple with 4 and 12
"""


def solution(l):

	k_factors = [0 for value in l] 	# stores the number of factors for each value
	lucky_triple_count = 0 			# how many lucky triples exist

	for k in range(1,len(l)):		# start at 2nd term since first term can't have any previous factors
		for j in range(0, k):		# look at terms from the first up to k-1 (any term that might be a factor)
			if l[k]%l[j] == 0:		# determine if j is a factor of k
				k_factors[k] +=1	# add 1 to the kth index
				lucky_triple_count += k_factors[j] # count is increased by the number of factors of the factor

	return lucky_triple_count		# return count



