# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

def get_No_of_Islands(grid):

    m = len(grid)  # row length of grid
    n =  len(grid[0]) # column lenght of grid

    NumOfIslands = 0 # varibale to track numerOfIslands


    # if grid is empty, return 0
    if ( m == 0 and n == 0):
        return 0

    # loop for every node of grid
    for i in range(m):
        for j in range(n):
            # Increase numerOfIslands count by 1 if a node has value as 1
            if (grid[i][j] == 1):
                NumOfIslands += 1
                ConvertGroundToWater(grid,i,j)

    return NumOfIslands

def ConvertGroundToWater(grid,i,j):

    # below edge cases to be handled where no action needed
        # Out of boundary --> return 0
        # node value is 0

    if ( i >= len(grid)  or j >= len(grid[0]) or i < 0 or j < 0 ) or (grid[i][j] == 0 ) :
        return
    else:
        grid[i][j] = 0

    # call recursive function to make all next connected nodes to 0
    # in order not to count duplicate in island count as these are connected node
    ConvertGroundToWater(grid, i, j - 1) # left
    ConvertGroundToWater(grid, i, j + 1) # right
    ConvertGroundToWater(grid, i-1, j) # up
    ConvertGroundToWater(grid, i+1, j) # down


def main():

    global grid

    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,1]
        ]

    print("Number of Islands are" , get_No_of_Islands(grid))

if __name__ == "__main__":
    main()