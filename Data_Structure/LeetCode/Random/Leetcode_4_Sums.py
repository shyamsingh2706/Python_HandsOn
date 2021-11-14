# https://leetcode.com/problems/4sum/
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

class Solution:
    def fourSum(self, nums: list[int],target) -> list[int]:

        # first Sort an array
        sort_nums = sorted(nums)
        print(sort_nums)
        res = []

        # llop through Array
        for idx, val in enumerate(sort_nums):
            # if Index i greater than 0 and previous value is same as current
            if idx > 0 and val == sort_nums[idx - 1]:
                continue

            # keep 3 pointers , next,Left & right
            for j in range(idx+1,len(sort_nums)):

                if j > idx+1 and sort_nums[j] == sort_nums[j - 1]:
                    continue

                next = j
                left = next+1
                right = len(sort_nums) - 1

                # llop through it
                while left < right:
                    foursum = val + sort_nums[next] + sort_nums[left] + sort_nums[right]
                    if foursum > target:
                        right = right - 1
                    elif foursum < target:
                        left = left + 1
                    elif foursum == target:
                        res.append([val,sort_nums[next],sort_nums[left], sort_nums[right]])
                        # once captured the results, Update the pointer
                        left = left + 1
                        while sort_nums[left] == sort_nums[left - 1] and left < right:
                            left = left + 1

        return res


def main():
    nums = [-2,-1,-1,1,1,2,2]
    target = 0
    s = Solution()
    res = s.fourSum(nums,target)
    print(res)


main()