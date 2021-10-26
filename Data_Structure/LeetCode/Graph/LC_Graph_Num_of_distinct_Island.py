# https://www.geeksforgeeks.org/find-the-number-of-distinct-islands-in-a-2d-matrix/

# Given a boolean 2D matrix. The task is to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is equal to another (not rotated or reflected).
# Examples:

# Input: grid[][] =
# {{1, 1, 0, 0, 0},
# 1, 1, 0, 0, 0},
# 0, 0, 0, 1, 1},
# 0, 0, 0, 1, 1}}

# Output: 1
# Island 1, 1 at the top left corner is same as island 1, 1 at the bottom right corner
import numpy as np


def get_No_of_Islands(grid):

    m = len(grid)  # row length of grid
    n =  len(grid[0]) # column lenght of grid

    # setting variable to compute navigation path for each island
         # X start , O Out of bound or Water
         # L left , R Right , U up, Down D

    # using these varibales , we can capture entire path for each Island calculation navigation
    # we can store it in Set and set size will be number of Unique Island

    Distinct_Island = set()

    # if grid is empty, return 0
    if ( m == 0 and n == 0):
        return 0

    # loop for every node of grid
    for i in range(m):
        for j in range(n):
            # Increase numerOfIslands count by 1 if a node has value as 1
            if (grid[i][j] == 1):
                path = ComputePath(grid,i,j,'X')
                Distinct_Island.add(path)

    return len(Distinct_Island)

def ComputePath(grid,i,j,path):

    # below edge cases to be handled where no action needed
        # Out of boundary --> return 0
        # node value is 0

    if ( i >= len(grid)  or j >= len(grid[0]) or i < 0 or j < 0 ) or (grid[i][j] == 0 ) :
        return 'O'
    else:
        grid[i][j] = 0

    # call recursive function to make all next connected nodes to 0
    # in order not to count duplicate in island count as these are connected node
    left = ComputePath(grid, i, j - 1,'L') # left
    right = ComputePath(grid, i, j + 1,'R') # right
    up = ComputePath(grid, i-1, j,'U') # up
    down = ComputePath(grid, i+1, j,'D') # down

    return path + left + right + up + down

def main():

    global grid
    global Island
    Island = []

    grid = [
        [1,1,0,0,1],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
        ]


    print("Number of Unique Islands are" , get_No_of_Islands(grid))

if __name__ == "__main__":
    main()