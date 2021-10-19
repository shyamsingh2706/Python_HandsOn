# https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/325-maximum-size-subarray-sum-equals-k.html

# Given an array containing N positive integers and an integer K.
# Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.

# Example 1: Given nums = [1, -1, 5, -2, 3], k = 3, return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
#
# Example 2: Given nums = [-2, -1, 2, 1], k = 1, return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

def largest_SubArray_of_sum(arr,k):

    start = 0
    end = 0
    window_size = 0
    sum = 0

    while ( end < len(arr) ) :

        sum = sum + arr[end]

        if sum < k :
            end += 1
        elif sum == k :
            window_size = max(window_size,end-start+1)
            end += 1
        # if sum is crossing the predefined Sum
        # remove elements until subarrray sum is less than pre-defined sum
        elif sum > k:
            while sum > k:
                sum = sum - arr[start]
                start += 1
            end += 1

    return window_size

def main():

    arr = [4 ,1 ,1, 1, 2, 3, 5]
    k = 5
    print("Max Sum Subarray of size K  is " , largest_SubArray_of_sum(arr,k))

if __name__ == "__main__":
    main()