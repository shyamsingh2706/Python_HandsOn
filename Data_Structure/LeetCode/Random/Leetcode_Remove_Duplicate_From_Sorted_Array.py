# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
# each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums. More formally,
# if there are k elements after removing the duplicates, then the first k elements of nums should hold the
# final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 0
        set_nums = set()
        for i in nums:
            if i not in set_nums:
                nums[index] = i
                index += 1

            set_nums.add(i)

        return index

def main() :

    nums = [0,0,1,1,1,2,2,3,3,4]
    S = Solution()
    res = S.removeDuplicates(nums)
    print(res)

if __name__ == "__main__":
    main()