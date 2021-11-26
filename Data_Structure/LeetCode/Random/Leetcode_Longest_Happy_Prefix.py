# https://leetcode.com/problems/longest-happy-prefix/
# A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
# Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
# and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".


class Solution:

    def longestPrefix_BF(self, s: str) -> str:

        res = ''
        for i in range(1, len(s)):
            if s[:i] == s[-i:]:
                res = s[:i]
        return res

    def longestPrefix(self, s: str) -> str:

        prefix, suffix = s[:-1], s[1:]
        #print ( prefix, suffix )
        while prefix and suffix and prefix != suffix:
            prefix = prefix[:-1]
            suffix = suffix[1:]
            #print ( prefix, suffix )
        return prefix



def main():

    strs = "level"
    s = Solution()
    print(s.longestPrefix(strs))

if __name__ == "__main__":
    main()
