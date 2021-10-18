#https://leetcode.com/problems/k-closest-points-to-origin/

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# as its against origin i.e. (0,0 ) , Euclidean distance will be √(X)2 + (Y)2).

import heapq
import numpy as np

def k_closest_point(arr,k):

    dist_arr = []
    heap = []

    for i in range(len(arr)):
        dist = np.sqrt( np.square(arr[i][0]) + np.square(arr[i][1]))
        heapq.heappush(heap,(-dist,i)) ## Building Max Heap as we need Closest element.
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    while heap:
        res.append(arr[heapq.heappop(heap)[1]])

    return res

def main():

    heap = [[3,3],[5,-1],[-2,4]]
    k= 2

    print(k_closest_point(heap,k))


if __name__ == "__main__":
    main()