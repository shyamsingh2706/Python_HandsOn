# https://leetcode.com/problems/decode-ways/
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
    # 'A' -> "1"
    # 'B' -> "2"
    # ...
    # 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def numDecodings(self, s: str) -> int:

        if len(s) == 0:
            return 0

        dp = [0] * (len(s)+1)
        dp[0] = 1

        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2,len(s)+1):
            # Always check for 2 Digt max as we cant go beyond 2 digit
            one_digit = int(s[i-1:i])
            two_digit = int(s[i-2:i])
            if one_digit >= 1 :
                dp[i] += dp[i-1]
            if two_digit >= 10 and two_digit <= 26 :
                dp[i] += dp[i-2]

        return dp[len(s)]

def main():

    s = "226"
    sol = Solution()
    print(sol.numDecodings(s))

if __name__ == "__main__":
    main()