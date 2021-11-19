# https://leetcode.com/problems/monotonic-array/
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return False

        if len(nums) <= 2:
            return True

        idx = 0
        is_ascending = 'N'

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                idx = i
                if nums[i - 1] > nums[i]:
                    is_ascending = 'N'
                else:
                    is_ascending = 'Y'

                break

        for i in range(idx, len(nums)):

            if is_ascending == 'N':
                if not (nums[i] <= nums[i - 1]):
                    return False

            elif is_ascending == 'Y':
                if not (nums[i] >= nums[i - 1]):
                    return False

        return True


def main() :

    nums = [1,2,2,3]
    s = Solution()
    print(s.isMonotonic(nums) )

if __name__ == "__main__":
    main()