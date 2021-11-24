# https://leetcode.com/problems/sort-array-by-parity/

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Example 1:
#
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums

        index = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                # swap Element
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        return nums


def main():

    nums = [3,1,2,4]

    sol = Solution()
    print(sol.sortArrayByParity(nums))

if __name__ == "__main__":
    main()