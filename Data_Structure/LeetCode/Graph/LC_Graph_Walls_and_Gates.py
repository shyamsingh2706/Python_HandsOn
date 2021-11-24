# https://leetcode.ca/all/286.html

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF
# as you may assume that the distance to a gate is less than 2147483647.

# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.

# Example:
# Given the 2D grid:

# INF  -1    0   INF
# INF  INF  INF  -1
# INF  -1   INF  -1
# 0    -1   INF  INF

# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

def wallsGates(grid):

    rows = len(grid)
    cols = len(grid[0])
    dist = 0
    for i in range(rows):
        for j in range(cols):
            # if found 0 , start navigating for all the nodes
            if grid[i][j] == 0:
                populateGrid(grid,i,j,rows,cols,dist)

    return grid

def populateGrid(grid,i,j,rows,cols,dist):

    # check border line condition
    # alos check if previous count that was updated in case node is visited
    # should be updated if current distance is less that already updated distance , else it will overwrite
    if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] < dist :

        return

    # update node with current distance
    grid[i][j] = dist

    # navigate in all directions 
    populateGrid(grid,i-1,j,rows,cols,dist+1)
    populateGrid(grid, i + 1, j, rows, cols, dist+1)
    populateGrid(grid, i , j-1, rows, cols, dist+1)
    populateGrid(grid, i , j+1, rows, cols, dist+1)


def main():

    global grid

    grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]

    print(wallsGates(grid))

if __name__ == "__main__":
    main()