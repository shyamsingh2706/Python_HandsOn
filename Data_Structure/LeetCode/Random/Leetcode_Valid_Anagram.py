
# https://leetcode.com/problems/valid-anagram/
# https://leetcode.com/problems/valid-anagram/

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


def main():

    str1 =   'anagram'
    str2=  'nagaram'
    s = Solution()
    res = s.isAnagram(str1,str2)
    print(res)

if __name__ == "__main__":
    main()