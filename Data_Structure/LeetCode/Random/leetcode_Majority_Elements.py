# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

import collections
def majorityElement( nums: list[int]) -> int:
    num_dict = collections.Counter(nums)
    for i in num_dict.keys():
        if num_dict[i] > len(nums) // 2:
            return i

    return -1


def main():

    arr = [3,2,3]
    print(majorityElement(arr))


if __name__ == "__main__":
    main()