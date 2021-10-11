import sys
import numpy as np

# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

def isPalindrome(str, i, j):

    if i == j : # Single element String
        return True
    elif i > j : # Empty string
        return True
    else:
        while j > i :
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1
        return True


def min_Palindrome_Partion_recurssion (str, i, j):

    max_partition = sys.maxsize

    if i >= j or isPalindrome(str, i, j) :
        return 0

    for k in range(i,j):
        temp_partition_count = 1 + min_Palindrome_Partion_recurssion(str,i,k) + min_Palindrome_Partion_recurssion(str,k+1,j)
        max_partition = min(max_partition,temp_partition_count)

    return max_partition

def min_Palindrome_Partion_memoization (str, i, j):

    max_partition = sys.maxsize

    if i >= j or isPalindrome(str, i, j) :
        return 0

    if dp[i][j] != -1 :
        return dp[i][j]

    for k in range(i,j):
        temp_partition_count = 1 + min_Palindrome_Partion_recurssion(str,i,k) + min_Palindrome_Partion_recurssion(str,k+1,j)
        max_partition = min(max_partition,temp_partition_count)
        dp[i][j] = max_partition

    return dp[i][j]

def min_Palindrome_Partion_memoization_Optimized (str, i, j):

    max_partition = sys.maxsize

    if i >= j or isPalindrome(str, i, j) :
        return 0

    if dp[i][j] != -1 :
        return dp[i][j]

    for k in range(i,j):

        if dp[i][k] != -1 :
            left = dp[i][k]
        else:
            left = min_Palindrome_Partion_recurssion(str,i,k)
            dp[i][k] = left

        if dp[k+1][j] != -1 :
            right = dp[k+1][j]
        else:
            right = min_Palindrome_Partion_recurssion(str,k+1,j)
            dp[k+1][j] = right

        temp_partition_count = 1 + left  + right
        max_partition = min(max_partition,temp_partition_count)
        dp[i][j] = max_partition

    return dp[i][j]

def main():


    str = "ababbbabbababa"

    global dp
    dp = np.full((1001, 1001), -1).tolist()

    ## For any palindrome to be considered ,   i should be 0 as even one element can be treated as palindrome string
    # so I should be 0 and J should be Len(arr) - 1 ( keeping array Index in mind )
    # so either K should vary from i to J-1 i.e. loop should be between i to K and from K+1 to j
    # or        K should vary from i+1 to J i.e. loop should be between i to k-1 and from k to j

    print(
        "Min cuts needed for Palindrome Partitioning through recurrsion ",
        min_Palindrome_Partion_recurssion(str, 0, len(str) - 1),
    )

    print(
        "Min cuts needed for Palindrome Partitioning through DP memoization ",
        min_Palindrome_Partion_memoization(str, 0, len(str) - 1),
    )

    print(
        "Min cuts needed for Palindrome Partitioning through DP memoization Optimized Approach is ",
        min_Palindrome_Partion_memoization_Optimized(str, 0, len(str) - 1),
    )

if __name__ == "__main__":
    main()