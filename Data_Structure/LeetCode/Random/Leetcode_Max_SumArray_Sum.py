# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6


import sys

def maximum_subarray_sum(arr):

    max_sum = -sys.maxsize
    sum = 0
    for j in arr:

        sum = max(sum + j, j)
        max_sum = max(max_sum,sum)

    return max_sum

def main():

    arr = [-2,1,-3,4,-1,2,1,-5,4]

    print("maximum_subarray sum is  is " , maximum_subarray_sum(arr))

if __name__ == "__main__":
    main()