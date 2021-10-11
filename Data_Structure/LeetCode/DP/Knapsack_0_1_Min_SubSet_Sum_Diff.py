import numpy as np
import sys

## Refer mentioned link for details https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
## to find minimum difference in 2 subset of given array
## S1 - S2 = Min ===> ( Array Sum - S2 ) - S2 = Min
## Array Sum - 2*S2 = Min  i.e. Sum of S2 or S1 should be closed to Array Sum / 2 in order to find minimum differece in S1 or S2

# As part of Minimum Subset Sum we already populated a DP matrix to find out if a given Sum is possible using a array subset
# if we access the closest True element of this matrix in Input_list_len+1 row of DP matrix thats less than or equal to array Sum / 2
# We can find respective column value as minimum subset difference for a given array

def Min_SubSet_Sum_Diff(Input_list,Target,Input_list_len) :

    dp_rows = Input_list_len + 1
    dp_columns =  Target + 1
    dp = np.full((dp_rows,dp_columns),False).tolist()


    for i in range(dp_rows):
        for j in range(dp_columns):
            if j == 0 :
                dp[i][j]= True
            if i == 0 :
                dp[i][j]= False

    for i in range(1,dp_rows):
        for j in range(1,dp_columns):

            if Input_list[i-1] > j :
                dp[i][j]= dp[i-1][j]
            elif Input_list[i-1] <= j :
                dp[i][j] = ( (dp[i-1][j])  or (dp[i-1][j - Input_list[i-1]]) )
    #print (dp)
    return dp

def Min_SetSet_Sum_diff(Input_list,Input_list_len) :


    arr_sum = 0
    for j in Input_list:
        arr_sum += j

    #print (arr_sum)
    dp_arr = Min_SubSet_Sum_Diff(Input_list, arr_sum, Input_list_len)
    #print (dp_arr)
    # Initialize difference
    # of two sums.
    diff = sys.maxsize

    # Find the largest j such that dp_arr[Input_list_len+1][j]
    # is true where j loops from sum/2 t0 0
    for j in range(arr_sum//2 , -1 ,-1) :
        if dp_arr[Input_list_len][j] == True :
            diff = arr_sum - ( 2 * j )
            break
    return diff

def main() :

    Input_list = [3,4,5,1,1]
    Input_list_len = len(Input_list)

    print("The minimum difference between 2 sets is ", Min_SetSet_Sum_diff(Input_list, Input_list_len))

if __name__ == "__main__" :
    main()