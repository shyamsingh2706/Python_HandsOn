#https://leetcode.com/problems/island-perimeter/

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.
import numpy as np

def IslandPerimeter(grid):

    rows = len(grid)
    cols = len(grid[0])

    # if grid is empty, return 0
    if (rows == 0 and cols == 0):
        return 0

    global visited
    visited = np.full((rows, cols), False).tolist()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return CalIslandPerimeter(grid,i,j,rows,cols,visited)
    return 0

def CalIslandPerimeter(grid,i,j,rows,cols,visited):

    # check for out of bound , return 1 as it has to be counted in perimeter
    if  i < 0 or j < 0 or i >= rows or j >= cols  :
        return 1

    # if not outbound
    else:

        # if node is 0 , count as perimeter
        if grid[i][j] == 0:
            return 1

        # if node is 1 and  is already visited
        # dont count in
        if (  grid[i][j] == 1 and visited[i][j] == True) :
            return 0


        # if not outbound and node is not visited and node is 1
        # mark as visited
        visited[i][j] = True

        # check its neibourhood nodes in all direction
        left = CalIslandPerimeter(grid,i,j-1,rows,cols,visited)
        right = CalIslandPerimeter(grid, i, j+1, rows, cols,visited)
        up = CalIslandPerimeter(grid, i-1, j, rows, cols,visited)
        down = CalIslandPerimeter(grid, i+1, j, rows, cols,visited)

        # return total parimeter sum
        return left+right+up+down

def main():

    global grid

    grid = [
            [0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]
            ]

    print("Island perimeter length is " , IslandPerimeter(grid))

if __name__ == "__main__":
    main()