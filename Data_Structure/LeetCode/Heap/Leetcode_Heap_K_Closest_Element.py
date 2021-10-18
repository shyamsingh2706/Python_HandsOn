#https://leetcode.com/problems/find-k-closest-elements/

# Given an unsorted array and two numbers x and k, find k closest values to x.
# Input : arr[] = {10, 2, 14, 4, 7, 6},
# x = 5, k = 3

import heapq

def find_k_closest_number(arr,x,k):

    heap =[]

    for idx,val in enumerate(arr):
        diff = -1 * abs( val - x) ## multiplying as have to build max heap to retain closest ( min ) elements
        temp_tuple = (diff,idx)
        heapq.heappush(heap,temp_tuple)
        if len(heap) > k :
            heapq.heappop(heap)

    result = []
    while heap:
        result.append(arr[heapq.heappop(heap)[1]])

    return result

def main():

    heap = [10, 2, 14, 4, 7, 6]
    k = 3
    x = 5
    print(find_k_closest_number(heap,x,k))


if __name__ == "__main__":
    main()