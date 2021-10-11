# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

def Array_Rotation_Count(arr):

    start = 0
    end = len(arr) - 1
    N =  len(arr)

    while end >= start :

        mid_element = (start+end) // 2
        next_element = (mid_element+1) % N
        prev_element = (mid_element+N-1) % N

        #arr_mid = arr[mid_element]
        #arr_prv = arr[prev_element]
        #arr_next = arr[next_element]
        #arr_start = arr[start]
        #arr_end = arr[end]

        #Checking if mid is minimum
        if arr[mid_element] < arr[prev_element] and arr[mid_element] <= arr[next_element]:
            return mid_element
        #if not move towards the unsorted part of array
        #If the minimum element is not at the middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
            # if already in Sorted array postion , return start position
            # If middle element is smaller than last element, then right half is sorted and  then the minimum element lies in left half i.e. end = mid_element-1
            # If middle element is greater than first element, then first half is sorted and then the minimum element lies in right half i.e. start = mid_element+1
        else:
            if arr[mid_element] >= arr[start] and arr[mid_element] <= arr[end]:
                return start
            elif arr[mid_element] >= arr[start]:
                start = mid_element + 1
            elif arr[mid_element] <= arr[end]:
                end = mid_element - 1


def main():
    # Driver Code
    arr = [13, 14, 15, 18, 20, 25, 2, 3, 6, 12]

    print("Number of Times array is right rotated ( Anti clockwise )  is : " , len(arr) - Array_Rotation_Count(arr) )
    print("Number of Times array is left rotated ( closkwise) is : ", Array_Rotation_Count(arr) )


if __name__ == "__main__":

    main()
