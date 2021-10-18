# https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/

# Given an array of integers and two numbers k1 and k2. Find the sum of all elements between given two k1’th and k2’th smallest elements of the array.
# It may be assumed that (1 <= k1 < k2 <= n) and all elements of array are distinct.


# Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6
# Output : 26
#          3rd smallest element is 10. 6th smallest element
#          is 20. Sum of all element between k1 & k2 is
#          12 + 14 = 26

# Input : arr[] = {10, 2, 50, 12, 48, 13}, k1 = 2, k2 = 6
# Output : 73

import heapq

def find_kth_min_element(arr,k):

    heap=[]

    for i in arr:
        heapq.heappush(heap,-i)
        if len(heap) > k:
            heapq.heappop(heap)

    return -1 * heapq.heappop(heap)

def sum_of_element_between_two_kth(arr,k1,k2):

    k1_element = find_kth_min_element(arr,k1)
    k2_element = find_kth_min_element(arr,k2)

    element_sum = 0

    for j in arr:
        if j > k1_element and j < k2_element:
            element_sum = element_sum + j

    return element_sum

def main():

    arr = [10, 2, 50, 12, 48, 13]
    k1 = 2
    k2 = 6
    print("Sum of all element between k1 & k2 is " , sum_of_element_between_two_kth(arr,k1,k2))

if __name__ == "__main__":
    main()