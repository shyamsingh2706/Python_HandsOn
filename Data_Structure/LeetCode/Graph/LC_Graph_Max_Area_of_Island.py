# https://leetcode.com/problems/max-area-of-island/

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: grid[][] =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# Output: 6

# Explanation: The answer is not 11, because the island must be connected 4-directionally.


import numpy as np


def Max_Area_of_Island(grid):

    m = len(grid)  # row length of grid
    n =  len(grid[0]) # column lenght of grid
    max_area = 0


    # if grid is empty, return 0
    if ( m == 0 and n == 0):
        return 0

    # loop for every node of grid
    for i in range(m):
        for j in range(n):
            # if grid position is 1, start calculating the Island area
            if (grid[i][j] == 1):
                area = ComputeArea(grid,i,j)
                # keep a tab of max Island area
                max_area = max(max_area,area)

    return max_area

def ComputeArea(grid,i,j):

    # below edge cases to be handled where no action needed
        # Out of boundary --> return 0
        # node value is 0

    if ( i >= len(grid)  or j >= len(grid[0]) or i < 0 or j < 0 ) or (grid[i][j] == 0 ) :
        return 0
    else:
        grid[i][j] = 0

    # call recursive function to make all next connected nodes to 0
    # in order not to count duplicate in island count as these are connected node
    left = ComputeArea(grid, i, j - 1) # left
    right = ComputeArea(grid, i, j + 1) # right
    up = ComputeArea(grid, i-1, j) # up
    down = ComputeArea(grid, i+1, j) # down

    # return the count of area in all direction plus its own area i.e. 1
    return 1+left+right+up+down

def main():

    global grid
    global Island

    grid = [
         [0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]


    print("Max Area of Islands is" , Max_Area_of_Island(grid))

if __name__ == "__main__":
    main()