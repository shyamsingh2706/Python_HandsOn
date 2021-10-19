# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1#
# Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.
# Input :
# N = 5
# A[] = {-8, 2, 3, -6, 10}
# K = 2

# Output :
# -8 0 -6 -6
# Explanation :
# First negative integer for each window of size k
# {-8, 2} = -8
# {2, 3} = 0 (does not contain a negative integer)
# {3, -6} = -6
# {-6, 10} = -6


import sys

def first_negative_int(arr,n,k):

    start = 0
    end = 0
    result = []
    temp_neg_list = []

    while end < n :

        if arr[end] < 0 :
            temp_neg_list.append(arr[end])

        if end - start +1 < k :  ## end - start +1 is the formula for window size
            # increase end pointer until we achive window size
            end += 1
        elif end - start +1 == k : # Once we achived window size

            if len(temp_neg_list) == 0 : # if no negative number exists return 0
                result.append(0)
            else:
                result.append(temp_neg_list[0]) # if list is not empty means , we have negative number
                if temp_neg_list[0] == arr[start] : # post adding check if start value is matching with negative Number first occurence
                    # if yes, delete the same
                    temp_neg_list.pop(0)

            start += 1  # increase start pointer
            end += 1  # increase end pointer to retain window size


    return result

def main():

    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    n = 8
    k = 3
    print("First negative integer in every window of size k " , first_negative_int(arr,n,k))

if __name__ == "__main__":
    main()