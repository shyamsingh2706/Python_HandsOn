# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: list[int]) -> list[int]:

        # first Sort an array
        sort_nums = sorted(nums)
        print(sort_nums)
        res = []

        # llop through Array
        for idx, val in enumerate(sort_nums):
            # if Index i greater than 0 and previous value is same as current
            if idx > 0 and val == sort_nums[idx - 1]:
                continue

            # keep two pointers , Left & right
            left = idx + 1
            right = len(sort_nums) - 1

            # llop through it
            while left < right:
                threeSum = val + sort_nums[left] + sort_nums[right]
                if threeSum > 0:
                    right = right - 1
                elif threeSum < 0:
                    left = left + 1
                else:
                    res.append([val, sort_nums[left], sort_nums[right]])
                    # once captured the results, Update the pointer
                    left = left + 1
                    while sort_nums[left] == sort_nums[left - 1] and left < right:
                        left = left + 1

        return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    res = s.threeSum(nums)
    print(res)


main()