# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down.
# You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9]

# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

import numpy as np
class Solution:

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        row = len(matrix)
        cols = len(matrix[0])
        global path_matrix
        # create a DP to story pre-calculated path for each node while first navigation to avoid doing same things over and over again
        path_matrix = np.full((row,cols),0).tolist()
        Longest_path = 0

        if row == 0 and cols == 0 :
            return 0

        # navigate to each node and calculate longest path for each node
        for i in range(row):
            for j in range(cols):
                 path = self.CalLongestIncresingPath(matrix,i,j,row,cols)
                 Longest_path = max(Longest_path,path)

        return Longest_path

    def CalLongestIncresingPath(self,matrix,i,j,row,cols):

        # check out memoization DP if pre-calculated path is already stored for a given node, return the same
        if path_matrix[i][j] > 0:
            return path_matrix[i][j]

        # else calculate path in each direction
        max_path = 0
        for direction in self.directions:

            x = direction[0] + i
            y = direction[1] + j

            if x > -1 and y > -1 and x < row and y < cols and matrix[x][y] > matrix[i][j]:
                longest = self.CalLongestIncresingPath(matrix,x,y,row,cols)
                # calculate Max path from all 4 direction and consider the same
                max_path = max(longest,max_path)

        # store the max path for that given node by adding 1 to it i.e. consider its own node count before returning the result to parent node
        path_matrix[i][j]= 1+max_path

        return path_matrix[i][j]


def main():


    Matrix = [[9,9,4],
              [6,6,8],
              [2,1,1]]

    s = Solution()

    print("Longes Increasing Path in given Matrix is" , s.longestIncreasingPath(Matrix))

if __name__ == "__main__":
    main()