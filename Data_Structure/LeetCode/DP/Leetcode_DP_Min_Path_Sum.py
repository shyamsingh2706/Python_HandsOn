# https://leetcode.com/problems/minimum-path-sum/
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right, which minimizes the sum of all numbers along its path.


import numpy as np
class Solution:

    def minPathSum(self, grid: list[list[int]]) -> int:

        n = len(grid)  # row length of grid
        m = len(grid[0])  # column lenght of grid

        array = np.full((n, m), 0).tolist()

        array[0][0] = grid[0][0]
        for j in range(1, m):  # fill in the first line
            array[0][j] = array[0][j - 1] + grid[0][j]

        for i in range(1, n):  # fill in the first column
            array[i][0] = array[i-1][0] + grid[i][0]
        # fill in our array, where the value of each cell corresponds to the shortest path to it
        for i in range(1, n):
            for j in range(1, m):
                array[i][j] = min(array[i][j - 1], array[i - 1][j]) + grid[i][j]

        #print(array)
        return array[n - 1][m - 1]


def main():

    grid = [[1,2,3],[4,5,6]]

    s = Solution()
    print("Min Path Sum is " , s.minPathSum(grid))

if __name__ == "__main__":
    main()