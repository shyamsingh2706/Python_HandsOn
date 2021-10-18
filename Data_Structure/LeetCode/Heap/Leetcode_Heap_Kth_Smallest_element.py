import heapq

def kth_smallest_element_NlogN(arr,k):

    ## Sorting is "N LogN" approach ( if Heap or merge sort will be consdered )
    arr.sort()
    return(arr[k-1])

def kth_smallest_element_NlogK(arr,k):

    # Apply Max Heap logic for Smallest element
    # Apply Min Heap logic for Largest Element

    # Creating Max Heap to find out Smallest Element
    # We will bound array size to kth element
    # and will return top element in end to find kth smallest element
    temp = []
    for j in arr:
     ## Applying negative sign to create max heap by default
        heapq.heappush(temp, -j)
        if len(temp) > k :
            heapq.heappop(temp)

    return -1 * heapq.heappop(temp)

def main():

    heap = [10,5,56,40,23,3,33]


    print(heap)

    k = 3 ## 3rd Smallest element
    print(kth_smallest_element_NlogK(heap,3))


if __name__ == "__main__":
    main()