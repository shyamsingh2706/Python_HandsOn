# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.
# N = 4, K = 2
# Arr = [100, 200, 300, 400]
# Output:  700
# Explanation:
# Arr3  + Arr4 =700,  which is maximum.
import sys

def sum_of_Subarray(arr,n,k):

    start = 0
    end = 0
    Max_sum = -sys.maxsize - 1
    sum = 0

    while end < n :
        sum = sum + arr[end]
        if end - start +1 < k :  ## end - start +1 is the formula for window size
            # increase end pointer until we achive window size
            end += 1
        elif end - start +1 == k : # Once we achived window size
            Max_sum = max(sum,Max_sum)  # take sum for a given window size
            sum = sum - arr[start] # remove start element from total sum as we will move window by one pointer
            start += 1  # increase start pointer
            end += 1  # increase end pointer to retain window size

    return Max_sum

def main():

    arr = [100, 200, 300, 400]
    n = 4
    k = 2
    print("Max Sum Subarray of size K  is " , sum_of_Subarray(arr,n,k))

if __name__ == "__main__":
    main()