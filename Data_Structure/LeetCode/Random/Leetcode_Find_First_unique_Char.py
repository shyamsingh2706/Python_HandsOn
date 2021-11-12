# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

import sys


class Solution():
    def firstUniqChar(self,str_arr):

        dict ={}
        min_index = sys.maxsize
        for i in str_arr:
            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i] += 1

        for idx in dict.keys():
            if dict[idx] == 1:
                min_index = min(min_index,str_arr.index(idx))

        if min_index > len(str_arr):
            return -1

        return min_index



def main() :

    arr = "loveleetcode"
    s = Solution()
    index  = s.firstUniqChar(arr)
    print ( "index for firstUniqChar is : ", index)
if __name__ == "__main__":
    main()