
from collections import deque

# Build Queue Class
class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

def get_No_of_Islands_BFS(grid):

    rows = len(grid)
    cols = len(grid[0])

    global directions
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    NumOfIslands = 0

    if rows == 0 and cols == 0 :
        return 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 :
                NumOfIslands += 1
                FillwithWater(grid,i,j,rows,cols)

    return NumOfIslands

def FillwithWater(grid,i,j,rows,cols):

    Q = Queue()
    # convert 2D into 1D index --> row_index * cols + col_index =  Q_val
    # convert 1D into 2D index --> row_index  = Q-val/cols , col_index = Q-val % cols

    Q.enqueue([i,j])
    grid[i][j] = 0

     # Start BFS
    while(not Q.is_empty()):

        index = Q.dequeue()
        row_index = index[0]
        col_index = index[1]

        # navigate in all directions
        for direction in directions:
            x = direction[0] + row_index
            y = direction[1] + col_index

            # if not outbound
            if x > -1 and x < rows and y > -1 and y  < cols and grid[x][y] == 1 :
                # if one is found in any of the directions , add in Queue for further navigation
                grid[x][y] = 0
                Q.enqueue([x,y])

def main():

    global grid

    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,1]
        ]

    print("Number of Islands are" , get_No_of_Islands_BFS(grid))

if __name__ == "__main__":
    main()