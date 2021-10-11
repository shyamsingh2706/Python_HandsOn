# https://www.includehelp.com/icp/maximum-value-in-a-bitonic-array.aspx

#Given a bitonic array find the maximum value of the array.
# An array is said to be bitonic if it has an increasing sequence of integers followed immediately by a decreasing sequence of integers.

# https://www.geeksforgeeks.org/find-element-bitonic-array/
# Also serach a given element in Biotonic array
 # Solution , to find this , when we have apeak element's index of Bitonis array
 # We can use to break the bitonic array into two part.
 # left part from arr[0] to arr[peak_element_index -1 ] --> asscending array
 # Right part from arr[peak_element_index] to arr[len(arr)-1] --> descending Array
 # apply binary search and find the element ( similar to find element in Sorted array )

def BS_Max_Element_bitonic_Array(arr,start,end):

    while end >= start:
        mid_element = (start+end) // 2
        ## Handle edge case as Boundary elements has only one neighbour
        if mid_element > 0 and mid_element < (len(arr) -1) :
            # Compare middle element with its neighbours
            if arr[mid_element] > arr[mid_element+1] and arr[mid_element] > arr[mid_element-1]:
                return arr[mid_element]

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

    return -1



def main():
    # Driver Code
    arr = [1,4,8,3,2]

    Max_element = BS_Max_Element_bitonic_Array(arr,0,len(arr)-1)
    print("Max element in Bitonic Array :" , Max_element)


if __name__ == "__main__":

    main()