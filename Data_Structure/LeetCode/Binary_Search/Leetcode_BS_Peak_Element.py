# https://leetcode.com/problems/find-peak-element/
#  https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

#A peak element is an element that is strictly greater than its neighbors.
#Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.

def BS_Peak_Element(arr,start,end):
    
    if len(arr) == 0:
        return
    elif len(arr) == 1:
        return 0
    
    while end >= start:
        mid_element = (start+end) // 2
        ## Handle edge case as Boundary elements has only one neighbour
        if mid_element > 0 and mid_element < (len(arr) -1) :
            # Compare middle element with its neighbours
            if arr[mid_element] > arr[mid_element+1] and arr[mid_element] > arr[mid_element-1]:
                return mid_element

            # If middle element is not peak and
            # its right neighbour is greater
            # than it, then right half must
            # have a peak element

            elif arr[mid_element+1] > arr[mid_element]:
                start = mid_element+1

            # If middle element is not peak and
            # its left neighbour is greater
            # than it, then left half must
            # have a peak element

            elif arr[mid_element-1] > arr[mid_element]:
                end = mid_element-1

        # handle edge case seperately given it will have only one neighbour
        elif mid_element == 0 :
            if arr[0] > arr[1]:
                return 0
            else:
                return 1
        elif mid_element == len(arr) - 1:
            if arr[-1] > arr[-2]:
                return len(arr) - 1
            else :
                return len(arr) - 2

def main():
    # Driver Code
    arr = [1, 3, 20, 4, 1, 0]

    peak_element = BS_Peak_Element(arr,0,len(arr)-1)
    print("Peak Element Index postion of given array is :" , peak_element)


if __name__ == "__main__":

    main()
