# https://leetcode.com/problems/reverse-string/
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) // 2
        while l < r:
            s[l], s[-l - 1] = s[-l - 1], s[l]
            l += 1

def main() :

    X = ["h","e","l","l","o"]
    S = Solution()
    S.reverseString(X)
    print(X)

if __name__ == "__main__":
    main()