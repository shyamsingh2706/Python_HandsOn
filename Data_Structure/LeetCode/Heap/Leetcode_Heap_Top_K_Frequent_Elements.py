# https://leetcode.com/problems/top-k-frequent-elements/


# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = collections.Counter(nums)
        heap = []

        for key in num_dict.keys():

            heapq.heappush(heap, [num_dict[key], key])

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i in range(len(heap)):
            res.append(heap[i][1])

        return res