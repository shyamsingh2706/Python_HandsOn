#https://leetcode.com/problems/k-th-symbol-in-grammar/
import numpy as np

# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
# Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

# N=1   0
# N=2   01
# N=3   0110
# N=4   01101001

# if we notice , total length of each N of 2 ^ N-1
# also first half of current N is exactly matching with previous N values
# also 2nd half of current half is compliment of first half of previous N

#Above logic will be used to derive recursion logic while reducing the output.


def solve(n,k):

    len = np.power(2,n-1)
    mid = len//2

    if n == 1 and k == 1:
        return 0

    if k <= mid and k > 0 :
        # if k value is less than mid, we can directly read it from previous N
        return (solve(n - 1, k))

    if k > mid and k <= len :
        # if k value is greater than mid, we can directly read it from previous N of corrsponding K-mid index and then inverse its value.
        return not(solve(n-1,k-mid))


def main():

    N = 4
    K = 5
    res = solve(N,K)

    if res == True:
        print(  " K-th Symbol in Grammar is " ,1)
    elif res == False:
        print(  " K-th Symbol in Grammar is " , 0)
    else:
        print(  " K-th Symbol in Grammar is " , res)

if __name__ == "__main__":
    main()

