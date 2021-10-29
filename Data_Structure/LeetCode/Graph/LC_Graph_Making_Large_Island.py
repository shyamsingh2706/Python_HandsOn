# https://leetcode.com/problems/making-a-large-island/

# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:


        # first assign each Unique Island a Unique ID
        IslandId = 2    # variable to perform this task , initializing from 2 as 0 & 1 is already present in Matrix and we want to avoid clash of numbers
        rows = len(grid)
        cols = len(grid[0])
        # create a map to capture the Size of each Unique Island
        island_size_Map = {}
        # varibale to capture max Island Size
        max_Island_size = 0

        # varibale to capture all Directions
        global directions
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        if rows == 0 and cols == 0:
            return 0


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # function to capture the unique Island and capture size of each Island
                    Island_size = self.GetIslandSize(grid,i,j,rows,cols,IslandId)
                    # capture size of max size of each Unique Islands
                    max_Island_size = max(max_Island_size, Island_size)
                    # store each Unique Island and its size in a map to avoid further navigation to calculate size when we convert 0 to 1
                    island_size_Map[IslandId] = Island_size
                    # increase Unique Island Number
                    IslandId += 1

        # loop through revised grid where only )s aer present and other 1s are modified to respective Island IDs
        for i in range(rows):
            for j in range(cols):
                # if found 0 , check in neighbour nodes if we have any connection with Island
                if grid[i][j] == 0:
                    # capture that in a set to avoid duplciate neighbour Island IDs
                    IslandSet = set()
                    for direction in directions:
                        x = direction[0] + i
                        y = direction[1] + j
                        if x >= 0 and y >= 0 and  x < rows and y < cols and grid[x][y] != 0:
                            # add Neighbour Island IDs into Set
                            IslandSet.add(grid[x][y])  # capturing the unique Island IDs that we have next to each 0

                    # navigate Set and calcualte total size if we cahnge 0 to 1
                    sum = 1 # initialize to 1 as current 0 that we are loking at will be changed to 1
                    for num in IslandSet:
                        val = island_size_Map[num]
                        sum = sum + val
                    #capture max size
                    max_Island_size = max(max_Island_size, sum)

        # return Max size
        return max_Island_size


    def GetIslandSize(self,grid,i,j,rows,cols,IslandId):

        # check for outbounds or if a node is already visited , it wont be 1 as It willbe updated with Island ID
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 1:
            return 0

        # update the 1 to respective Island ID
        grid[i][j] = IslandId
        # check in All direction and return Size of each Unique Island
        left = self.GetIslandSize(grid, i, j-1, rows, cols, IslandId)
        right = self.GetIslandSize(grid, i, j+1, rows, cols, IslandId)
        up = self.GetIslandSize(grid, i-1, j, rows, cols, IslandId)
        down = self.GetIslandSize(grid, i+1, j, rows, cols, IslandId)

        return 1 + left + right + up + down

def main():

    global grid

    grid = [[0,1,0,1,0],
            [1,1,0,0,1],
            [0,0,1,1,0]]

    s = Solution()

    print("Max Area Island posible is" , s.largestIsland(grid))

if __name__ == "__main__":
    main()
