# https://leetcode.com/problems/sort-array-by-increasing-frequency/

#Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
# If multiple values have the same frequency, sort them in decreasing order.

#Return the sorted array.

# Example 1:
#
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Example 2:

# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

import heapq
import collections

def freq_sort(arr):

    freq_dict = collections.Counter(arr)

    heap =[]
    for key in freq_dict.keys():

        ## Min heap for count as we have to build array in increasing order ,so least freq element should be on top.
        ## max Heap for Value attibute as If multiple values have the same frequency, sort them in decreasing order. Greater value should be on top

        heapq.heappush(heap,(freq_dict[key],-key))

    res = []
    while heap:
        freq,key = heapq.heappop(heap)
        res= res +  [-key] * freq

    return res

def main():

    arr = [2,3,1,3,2]
    print(freq_sort(arr))


if __name__ == "__main__":
    main()