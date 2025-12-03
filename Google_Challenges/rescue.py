"""
The problem: Given a square matrix, with values indicating the time to
get from the row's starting point (the diagonals) to the row with the
same index as the value (the third value in a row takes you to the
third row), find the greatest number of unique columns that can be
visited, starting from the first row and column and ending with the
last column, within a given time limit. Some values may be negative.
Any spot may be revisited.

(You are rescuing bunnies which are at each column beyond the 0th and
before the last. A 5x5 matrix would have 3 bunnies: bunny 0, bunny 1,
bunny 2. The last column represents the exit.)

The solution: Firstly, optimize the matrix. Find the shortest route to
each spot from a row's starting point using the Bellman Ford algorithm
(that is,(if distance from row A to row B to row C is shorter than row
A to row C, then row A to row C is modified to the smaller value).
Repeat until no more changes are made. From here, check each different
permutation of paths that obeys the time limit and keep track of how
many columns are visited in each one. If one path has more visited
columns the the previous most, it becomes the ideal path unless another
path overtakes it. Return all the columns between the 0th and last
column that were visited. 
"""

def solution(time, time_limit):
	# takes a square matrix and a time limit to find
	# the path that visits the most columns witin the limit

	size = len(time)  # size of matrix

	
	def bunny_matrix(size):
		# create a matrix that will show which columns have been
		# visited to get to any spot within the main matrix.
		# Excludes starting column and end column since we must 
		# start and end there (they start off with 0 bunnies)
		# This bunny_matrix starts off with each spot only showing
		# a list containing its column index - 1 (the bunny # there)
		bunnies = []
		for row in range(size):
			bunnies.append([])
			for spot in range(size):
				if spot == 0 or spot == size-1:
					bunnies[row].append([])
				else:
					bunnies[row].append([spot-1])
		return bunnies
	bunnies = bunny_matrix(size)

	
	def ideal_time(time, size):
		# optimizes any square matrix
		# finds shortest route to each spot from row's starting point using the Bellman Ford algorithm
		# (if distance from row A to row B to row C is shorter than row A to row C, then row A to row C 
		# is modified to the smaller value. Repeat until no changes are made.)
		
		change = True 
		while change == True:  # loop until no more changes made
			change = False
			for row in range(size):  
				for spot in range(size):  
					current = time[row][spot]  # current smallest found distance to spot
					for other in range(size):
						if time[row][other] + time[other][spot] < current:  
							# if shorter route available, update

							update = time[row][other] + time[other][spot] 
							time[row][spot] = update
							current = update

							bunnies[row][spot].extend(bunnies[row][other])  
							# update bunnies matrix as other bunnies/columns may have been visited to get there

							change = True

						if time[spot][spot] < 0:  
						# if the distance to a spot from that spot is negative, we can gain infinite time
						# simply by continually visiting it.
							return False
		
		# return optimized matrix after all updates completed
		return time
	
	time = ideal_time(time, size)
	# for row in time:
	# 	print(row)

	if not time:  # if infinite loop, all bunnies rescuable/columns visitable in time limit
		return [x for x in range(size-2)]
	
	# we now have an optimized time matrix and a bunny/column matrix showing which bunnies/columns are available at each spot


	def ideal_path():
		# finds path that contains most bunnies/columns within time limit


		def rest_of_path(start, time_remaining): 
			# finds all viable paths from start and tracks how many 
			# bunnies/coulmns were visited in each path

			for x in range(1,size-1):
				if x not in path:  					
					path.append(x)
					bunnies_collected.append(bunnies[start][x]) 				 
					time_remaining -= time[start][x]
					rest = rest_of_path(x, time_remaining) 
					if time_remaining - rest >= 0:
						return rest + time[start][x]
					else:
						path.pop()
						bunnies_collected.pop()
						time_remaining += time[start][x]
			return time[start][size-1]


		path_list = [] 	
		bunnies_collected_list = []
		
		# try all viable start points and create list of all viable paths,
		# along with bunnies collected/columns visited for that path
		for start in range(0, size-2):
			path = []
			bunnies_collected = []
			bunnies_collected.append(bunnies[0][0])
			rest_of_path(start, time_limit - time[0][start])
			bunnies_collected_list.append(set([x[i] for x in bunnies_collected for i in range(len(x))]))
			path_list.append(path)

		# find path that has most bunnies collected/columns visited
		max_path = []
		for buns in bunnies_collected_list:
			if len(buns) > len(max_path):
				max_path = buns

		return max_path

	max_path = ideal_path()
	
	return [x for x in max_path]
