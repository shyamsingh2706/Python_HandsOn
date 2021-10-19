# https://www.interviewbit.com/problems/sliding-window-maximum/#

# Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1]
# For Example

# Input 1:
#     A = [1, 3, -1, -3, 5, 3, 6, 7]
#     B = 3
# Output 1:
#     C = [3, 3, 5, 5, 6, 7]

import sys

def sliding_window_max(arr,k):

    start = 0
    end = 0
    max_element = -sys.maxsize - 1
    max_element_arr = []
    result = []

    while end < len(arr) :

        # capture max element for a given window
        # 1) First Insert a new element
        # 2) Compare against max and reset max element
        # 3) pop all element from array that are less than max element so that max element is always on top
        max_element_arr.append(arr[end])
        max_element = max(max_element,arr[end])
        while max_element_arr[0] < max_element:
            max_element_arr.pop(0)

        if end - start +1 < k :  ## end - start +1 is the formula for window size
            # increase end pointer until we achive window size
            end += 1
        elif end - start +1 == k : # Once we achived window size
            result.append(max_element_arr[0])  # take latest max element for a given window
            if arr[start] ==  max_element_arr[0]: # if max element is the element where previous window was started
                # delete the same from array
                max_element_arr.pop(0)
                # repoint max element to next element of new window
                max_element = max_element_arr[0]
            start += 1  # increase start pointer
            end += 1  # increase end pointer to retain window size

    return result

def main():

    arr = [1, 3, -1, -3, -2, 5, 3, 6, 7]
    k = 3
    print("Sliding Window Maximum  is " , sliding_window_max(arr,k))

if __name__ == "__main__":
    main()