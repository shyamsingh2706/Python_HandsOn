import sys
import numpy as np

# https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
# Given a sequence of matrices, find the most efficient way to multiply these matrices together

def MCM_Solution_Recurrsion( Input_Arr , i , j ) :

    if ( i >= j ):
        return 0

    min_cost = sys.maxsize

    for k in range(i,j) :

        # if array is 40 20 30 10 30
        # for i to k ( if k is at 30 elemement ) , Matrix will be 40*20 & 20 * 30 --> 40*20*30
        # for k+1 to j ( if k is at 30 elemement ) , Matrix will be 30* 10 & 10*30  --> 30*10*30
        # now to calculat total cost, above two has to be summed up for which cost will be 40*30*30 --> array[i-1] * array[k] * array[j]
        # Same formula is applied below
        temp = MCM_Solution_Recurrsion(Input_Arr,i,k) + MCM_Solution_Recurrsion(Input_Arr,k+1,j) + Input_Arr[i-1]*Input_Arr[k]*Input_Arr[j]

        if(min_cost > temp):
            min_cost = temp

    return min_cost

def MCM_Solution_Memoization( Input_Arr , i , j ) :

    if ( i >= j ):
        return 0

    if dp[i][j] != -1 :
        return dp[i][j]

    dp[i][j] = sys.maxsize

    for k in range(i,j) :

        # if array is 40 20 30 10 30
        # for i to k ( if k is at 30 elemement ) , Matrix will be 40*20 & 20 * 30 --> 40*20*30
        # for k+1 to j ( if k is at 30 elemement ) , Matrix will be 30* 10 & 10*30  --> 30*10*30
        # now to calculat total cost, above two has to be summed up for which cost will be 40*30*30 --> array[i-1] * array[k] * array[j]
        # Same formula is applied below
        temp = MCM_Solution_Memoization(Input_Arr,i,k) + MCM_Solution_Memoization(Input_Arr,k+1,j) + Input_Arr[i-1]*Input_Arr[k]*Input_Arr[j]

        if(dp[i][j] > temp):
            dp[i][j] = temp

    return dp[i][j]

def main():

    arr = [40,20,30,10,30]
    global dp
    dp = np.full((1001,1001),-1).tolist()

    ## For Matrix to be considered , two elements to be considered always.
    # so first Matrix size should be i-1 to i and Last matrix Size should be j-1 to j
    # so I should be 1 and J should be Len(arr) - 1 ( keeping array Index in mind )
    # so either K should vary from i to J-1 i.e. loop should be between i to K and from K+1 to j
    # or        K should vary from i+1 to J i.e. loop should be between i to k-1 and from k to j

    i = 1
    j = len(arr) - 1

    print("Minimum number of multiplications through recurrsion approach is ", MCM_Solution_Recurrsion(arr,i,j))
    print("Minimum number of multiplications through Memoization approach is ", MCM_Solution_Memoization(arr, i, j))

if __name__ == "__main__":
    main()