# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome( s: str) -> str:
    ans = []
    for i in range(len(s)):
        start = i
        end = len(s)
        while start <= end:
            temp = s[start:end]
            ## Compare
            if temp == temp[::-1]:
                if len(temp) > len(ans):
                    ans = temp
            end -= 1
    return ans


output = longestPalindrome('abacdfgdcaba')
print(output)

# Time complexity : O(n^3)
# Space complexity : O(1)