#https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        # Bitwise operation
        # 1 xor 1 gives 0. 2 xor 2 gives 0
        # what it means 1 xor 1, 2 xor 2, 3 xor 3 will always give you 0
        # [4,1,2,1,2] - > [4] will stay as 4 [1,2,1,2] will cancel each other.
        # T: O(N)
        # S: O(1)

        combined = 0
        for i in nums:
            combined ^= i
            print (combined,i)
        return combined

def main():

    nums =[4,1,2,1,2]
    s = Solution()
    res = s.singleNumber(nums)
    print(res)

if __name__ == "__main__":
    main()