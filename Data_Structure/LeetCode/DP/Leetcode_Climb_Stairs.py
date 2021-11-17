# https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

def main() :

    n = 3
    S = Solution()
    res = S.climb(n)
    print(res)

if __name__ == "__main__":
    main()