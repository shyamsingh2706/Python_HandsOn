# https://leetcode.com/problems/unique-paths/
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int,op = 0 ) -> int:

        dp = np.full((m,n),0).tolist()

        # There is only one way for every row to reach 0th column
        for i in range(m):
            dp[i][0] = 1

        # There is only one way for every column to reach 0th row
        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]

def main():
    m = 3
    n = 2
    sol = Solution()
    res = sol.uniquePaths(m,n)
    print(res)

if __name__ == "__main__":
    main()