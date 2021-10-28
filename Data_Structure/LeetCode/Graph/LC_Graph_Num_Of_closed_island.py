# https://leetcode.com/problems/number-of-closed-islands/

# Given a 2D grid consists of 0s (land) and 1s (water).
# An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.


def get_No_of_closed_Islands(grid):

    rows = len(grid)
    cols = len(grid[0])

    closed_island_num = 0

    if rows == 0 and cols == 0:
        return 0
 
    # we dont have to check perimater of grid
    # if any element is present on perimeter, it cant be a closed island
    # close island means land is surrounded by water and all out of bound  and cant be considered as closed Island
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if grid[i][j] == 0:
                if is_closed_island(grid,i,j,rows,cols):
                    closed_island_num += 1

    return closed_island_num

def is_closed_island(grid,i,j,rows,cols):

    # -1 means its visited
    # 1 means water
    # 0 is land

    # if we encounter -1 or 1 , that means its a closed island thusfar
    if (grid[i][j] == -1 or grid[i][j] == 1):
        return True

    # if we passed above if clause , means we are encountred with 0 and we are on a land
    # check if current element is on perimeter or not.
    if i == 0 or j == 0 or i == rows-1 or j == cols-1:
        # if this result into True that means this element is on Perimeter
        # return False
        return False

    # if not on parimeter and not visited yet
    grid[i][j] = -1

    left = is_closed_island(grid,i,j-1,rows,cols)
    right = is_closed_island(grid, i, j+1, rows, cols)
    up = is_closed_island(grid, i-1, j, rows, cols)
    down = is_closed_island(grid, i+1, j, rows, cols)

    # checking and condition as even if one end is flase means Islans is not a closed Island
    return (left and right and up and down )

def main():

    global grid

    grid =  [[1,1,1,1,1,1,1,0],
             [1,0,0,0,0,1,1,0],
             [1,0,1,0,1,1,1,0],
             [1,0,0,0,0,1,0,1],
             [1,1,1,1,1,1,1,0]]

    print("Number of Islands are" , get_No_of_closed_Islands(grid))

if __name__ == "__main__":
    main()