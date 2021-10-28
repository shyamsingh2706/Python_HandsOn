#https://leetcode.com/problems/island-perimeter/

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.
import numpy as np

class Solution:
    def islandPerimeter(self,grid:list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # if grid is empty, return 0
        if (rows == 0 and cols == 0):
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return self.__CalIslandPerimeter(grid,i,j,rows,cols)
        return 0

    def __CalIslandPerimeter(self,grid,i,j,rows,cols):

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
            if (  grid[i][j] == -1) :
                return 0


            # if not outbound and node is not visited and node is 1
            # mark as visited
            grid[i][j] = -1

            # check its neibourhood nodes in all direction
            left = self.__CalIslandPerimeter(grid,i,j-1,rows,cols)
            right = self.__CalIslandPerimeter(grid, i, j+1, rows, cols)
            up = self.__CalIslandPerimeter(grid, i-1, j, rows, cols)
            down = self.__CalIslandPerimeter(grid, i+1, j, rows, cols)

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

    sol = Solution()
    print("Island perimeter length is " , sol.islandPerimeter(grid))

if __name__ == "__main__":
    main()
