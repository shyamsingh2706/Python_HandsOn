#https://leetcode.com/problems/path-with-maximum-gold/

# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:

# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.

# DFS transversal

import numpy as np
def get_max_gold(grid):

    m = len(grid)  # row length of grid
    n =  len(grid[0]) # column lenght of grid

    max_sum = 0 # varibale to track max Sum for each node during DFS transversal
    # create a visited array same as grid where we need to keep a tab of the node already visited
    global visited
    visited = np.full((m,n),False).tolist()

    # if grid is empty, return 0
    if ( m == 0 and n == 0):
        return 0

    # loop for every node for DFS transversal
    for i in range(m):
        for j in range(n):
            # visit a node only if there is a non zero value
            if (grid[i][j] != 0):
                #print( grid[i][j])
                sum = findMaxGold(grid,i,j,m,n,visited)
                max_sum = max(sum,max_sum)

    return max_sum

def findMaxGold(grid,i,j,m,n,visited):

    # below edge cases to be handled
        # Out of boundary --> return 0
        # already visited node --> return 0
        # node value is 0 --> return 0

    if ( i >= m or j >= n or i < 0 or j < 0 ) or (grid[i][j] == 0 ) or (visited[i][j] == True ):
        return 0

    # mark a node as visited when we start itrating it
    visited[i][j] = True
    # call recursive function to keep a track of its left,right , up and down DFS path sum
    left = findMaxGold(grid, i, j - 1, m, n, visited)
    right = findMaxGold(grid, i, j + 1, m, n, visited)
    up = findMaxGold(grid, i-1, j , m, n, visited)
    down = findMaxGold(grid, i+1, j, m, n, visited)

    # Mark node as False while existing that node's DFS transversal
    visited[i][j] = False
    # pick max value among all and add the its own node value before returning
    node_max_sum = max(left,right,up,down) + grid[i][j]
    #print(left,right,up,down,grid[i][j])
    return node_max_sum

def main():

    grid = [[0,6,0],
            [5,8,7],
            [0,9,0]]
    print("max gold collected is" , get_max_gold(grid))

if __name__ == "__main__":
    main()