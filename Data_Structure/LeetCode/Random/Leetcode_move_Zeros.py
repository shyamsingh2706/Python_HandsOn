# https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        index = 0
        for i in nums:
            if i != 0:
                nums[index] = i
                index += 1

        for j in range(index,len(nums)):
            nums[j] = 0



def main():
    nums = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)



if __name__ == "__main__":

    main()