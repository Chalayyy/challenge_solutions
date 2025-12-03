"""
The Problem: 
Given a matrix (of height and width between 2-20) with 0's
representing passable space and 1's representing unpassable,
find the shortest pass from the start to finish (top left to bottom right)
considering any single 1 may be changed to a 0.

The Solution:
This is accomplished through Dijkstra's algorithm (assume infinite distance to a
spot until calculated otherwise).
In each case, a different 1 is changed to a 0. Whichever case presents the shortest
path is the solution. 
"""


def solution(grid):

	# define width and height of matrix
	width = len(grid[0])
	height = len(grid)

	# list of smallest paths found
	min_path = []

	# change one value in grid from 1 to 0 to see if smaller path available
	for a in range(0,height):
		for b in range(0, width):
			if grid[a][b] == 1:

				# temp change 1 grid value to see if path is smaller
				original_value = grid[a][b]
				grid[a][b] = 0
				
				# check if a spot has already been mapped to prevent unnecessary
				# backtracking
				checked_spots = []

				# make all unknown distances from starting point infinity as a
				# grid marking shortest distance from starting point to respective
				# spot in matrix 
				grid_dis = []
				for h in range(0, height):
					grid_dis.append([float("inf") for w in range(0,width)]) 

				# distance to starting point is starting point's distance
				grid_dis[0][0] = 1

				# perform dijsktra algorithm to find shortest distance 
				# on altered matrix
				while True:

					# find smallest distance from starting point in whole grid 
					# to continue moving from (excludes visited points)
					smallest_element = (min(grid_dis[x][y] 
						for x in range(0, height) for y in range(0,width)))
					
					# get index of smallest element for reference
					for x in range(0,height):
						for y in range(0, width):
							if smallest_element == grid_dis[x][y]:
								h = x
								w = y
					# add this spot to list of checked spots
					checked_spots.append((h,w))
					
					# if we reached the end, break loop to change new variable
					# and if path found, add it min_path list
					if h == height -1 and w == width-1:
						if grid_dis[h][w] != float("inf"):
							min_path.append(grid_dis[h][w])	
						break
					
					# initialize directions
					left = float("inf")
					right = float("inf")
					up = float("inf")
					down = float("inf")

					# if a spot is available in a direction, check if moving there
					# would make the distanceto that spot smaller than an earlier 
					# path to that spot. If so, it's distance is the distance to 
					# the previous spot plus this spot's distance value.
					if w < width-1 and not grid[h][w+1] and (h,w+1) not in checked_spots:
						grid_dis[h][w+1] = min(grid_dis[h][w+1], 
												grid_dis[h][w] + 1)
						right = grid_dis[h][w+1]

					if h < height -1 and not grid[h+1][w] and (h+1,w) not in checked_spots:
						grid_dis[h+1][w] = min(grid_dis[h+1][w], 
												grid_dis[h][w] + 1)
						down = grid_dis[h+1][w]

					if h > 0 and not grid[h-1][w] and (h-1,w) not in checked_spots:
						grid_dis[h-1][w] = min(grid_dis[h-1][w],
												grid_dis[h][w] + 1)
						up = grid_dis[h-1][w]

					if w > 0 and not grid[h][w-1] and (h,w-1) not in checked_spots:
						grid_dis[h][w-1] = min(grid_dis[h][w-1],
												grid_dis[h][w] + 1)
						left = grid_dis[h][w-1]

					# remove the visited spot by making its distance infinity
					grid_dis[h][w] = float("inf")
					
					# move to the spot of the smallest path
					if right == min(left, right, up, down):
						w+=1

					elif down == min(left, right, up, down):
						h+=1

					elif up == min(left, right, up, down):
						h-=1

					elif left == min(left, right, up, down):
						w-=1

				grid[a][b] = original_value
	return min(min_path)


# print(solution(([[0, 0, 0, 0, 0, 0], 
#                 [1, 1, 1, 1, 1, 0], 
#                 [0, 0, 0, 0, 0, 0], 
#                 [0, 1, 1, 1, 1, 1], 
#                 [0, 1, 1, 1, 1, 1], 
#                 [0, 0, 0, 0, 0, 0]])))
