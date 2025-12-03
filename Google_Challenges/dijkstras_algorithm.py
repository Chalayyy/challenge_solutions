"""
The problem:
Given an w x h matrix (as a list of lists), find the shortest path from [0][0] to [w-1][h-1]

The solution:
Use Dijkstra's Algorithm:
1. From the starting point, assume the distance to every other point infinite.
2. Calculate the total distance from the start to all points adjacent to the start.
3. Change the distance to the new calculated distance if it is lower than the previous value.
4. Select the smallest distance available as the new start point.
5. Repeat steps 2-5 until end condition met (the bottom right value reached)
"""


def solution(grid):

	# define width and height of matrix
	width = len(grid[0])
	height = len(grid)

	# make all unknown distances from starting point infinity as a grid marking shortest distance
	# from starting point to respective spot in matrix
	grid_dis = []
	for h in range(0, height):
		grid_dis.append([float("inf") for w in range(0,width)]) 

	# distance to starting point is starting point's distance
	grid_dis[0][0] = grid[0][0]

	while True:

		# find smallest distance from starting point in whole grid to continue moving from
		smallest_element = (min(grid_dis[x][y] for x in range(0, height) for y in range(0,width)))
		for x in range(0,height):
			for y in range(0, width):
				if smallest_element == grid_dis[x][y]:
					h = x
					w = y

		# if we reached the end, print distance and end loop
		if h == height -1 and w == width-1:
			print(f"\nTotal for shortest path = {grid_dis[h][w]}")
			break
		
		# display smallest distance to move from
		print(f"\nThe smallest element is: {smallest_element} at {h},{w}")

		# initialize directions
		left = float("inf")
		right = float("inf")
		up = float("inf")
		down = float("inf")

		# if a spot is available in a direction, check if moving there 
		# would make the distance to that spot smaller than an earlier 
		# path to that spot. If so, it's distance is the distance to 
		# the previous spot plus this spot's distance value.

		if w < width-1:
			grid_dis[h][w+1] = min(grid_dis[h][w+1], grid_dis[h][w] + min(grid[h][w+1], grid_dis[h][w+1]))
			right = grid_dis[h][w+1]

		if h < height -1:
			grid_dis[h+1][w] = min(grid_dis[h+1][w], grid_dis[h][w] + min(grid[h+1][w], grid_dis[h+1][w]))
			down = grid_dis[h+1][w]

		if h > 0:
			grid_dis[h-1][w] = min(grid_dis[h-1][w], grid_dis[h][w] + min(grid[h-1][w], grid_dis[h-1][w]))
			up = grid_dis[h-1][w]

		if w > 0:
			grid_dis[h][w-1] = min(grid_dis[h][w-1], grid_dis[h][w] + min(grid[h][w-1], grid_dis[h][w-1]))
			left = grid_dis[h][w-1]

		# remove the visited spot by making its distance infinity
		grid[h][w] = float("inf")
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

		print("Grid distances: ")
		for x in range(0, height):
			print(grid_dis[x])

# Example: 	
# solution(([1,2,3,4,5],
# 		  [3,5,2,7,8], 
# 		  [4,7,2,0,4], 
# 		  [7,3,7,2,0],
# 		  [10,6,13,6,1]))
