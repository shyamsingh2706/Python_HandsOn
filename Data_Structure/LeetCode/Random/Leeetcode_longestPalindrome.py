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

### Optimized Approach 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        
        for i in range(len(s)):
            # this is for odd length palindrome
            word1 = self.checkPalindrome(s, i, i)
            # this is for even length palindrome
            word2 = self.checkPalindrome(s, i, i+1)
            
            #word1 will be max length word from word1 and word2
            word1 = word1 if len(word1) >= len(word2) else word2 
            
            # compare word1 with our result
            result = word1 if len(word1) >= len(result) else result
            
        return result
    
    def checkPalindrome(self, s, lo, hi):
        # expand as long as 'lo' can grow to the left
        # and 'hi' and grow to the right and chracters at those index match
        while lo>=0 and hi<len(s) and s[lo]==s[hi]:
            lo -= 1
            hi += 1
        
        # return the slice from original string that starts from our last matched index of lo and hi. We don't increament hi because python slice goes up to ending index-1
        return s[lo+1:hi]
    
output = longestPalindrome('abacdfgdcaba')
print(output)

# Time complexity : O(n^3)
# Space complexity : O(1)
