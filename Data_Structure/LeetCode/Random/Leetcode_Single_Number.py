# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

import collections
class Solution():
    def singleNumber(self,nums):

        stack = set()
        for i in nums:
            if i in stack:
                stack.remove(i)
            else:
                stack.add(i)

        return stack.pop()


def main():

    arr =  [4,1,2,1,2]
    s = Solution()
    res = s.singleNumber(arr)
    print(res)

if __name__ == "__main__":
    main()