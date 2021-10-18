#https://www.geeksforgeeks.org/nearly-sorted-algorithm/

# Given an array of n elements, where each element is at most k away from its target position
# devise an algorithm that sorts in O(n log k) time.
# For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

# Example:
# Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
# k = 3
# Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

# more efficiently with the help of Heap data structure. Following is the detailed process that uses Heap.
    # 1) Create a Min Heap of size k+1 with first k+1 elements. This will take O(k) time (See this GFact)
    # 2) One by one remove min element from heap, put it in result array, and add a new element to heap from remaining elements.
# Removing an element and adding a new element to min heap will take log k time.
# So overall complexity will be O(k) + O((n-k) * log(k)).


import heapq

def sort_k_sorted_Array(arr,k):

    # List of first k+1 items
    heap = arr[:k + 1]
    # using heapify to convert list
    # into heap(or min heap)
    heapq.heapify(heap)

    # "rem_elmnts_index" is index for remaining
    # elements in arr and "target_index" is target index of for current minimum element
    # in Min Heap "heap".
    target_index = 0
    for rem_elmnts_index in range(k + 1, len(arr)):
        arr[target_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[rem_elmnts_index])
        target_index += 1

    while heap:
        arr[target_index] = heapq.heappop(heap)
        target_index += 1

    return arr

def main():

    heap = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    print(sort_k_sorted_Array(heap,3))


if __name__ == "__main__":
    main()