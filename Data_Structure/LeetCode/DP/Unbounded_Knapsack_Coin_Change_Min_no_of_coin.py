import numpy as np
import sys

## https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
## https://www.youtube.com/watch?v=I-l6PBeERuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=16 video explanation

def Unbounded_knapsack_Coin_Change_Min_No_of_Coin (Input_list_wt,Target,Input_list_len):

    dp_rows = Input_list_len + 1
    dp_columns = Target + 1

    dp = np.full((dp_rows,dp_columns),0).tolist()

    ## Unique Initialization reason
    for i in range(dp_rows):
        for j in range(dp_columns):
            if j == 0 :
                dp[i][j] = 0 ## even if input is present , to get sum as 0 we need 0 coins
            elif i == 0 :
                dp[i][j] = sys.maxsize -1  ## if input is empty, to get sum of 0 or 1 or 2 etc.. we need infinity coins theoritically i.e. same as Int Max size

    ### Initialize the DP  Matrix for first input array element
    ## To check if target sum can be achived using first element of array or not to  navigate futher

    for j in range(1,dp_columns):
        if  j % Input_list_wt[0] == 0 : ## If target sum can be achieved using first array element
            dp[1][j] = j // Input_list_wt[0] ## intialize number of time the coin needed to achive target sum
        else :
            dp[1][j] = sys.maxsize - 1  ## -1 is being done in Int Max size becuase when we consider +1 while considering the coin, it might cause overflow

    print(dp)

    for i in range(1,dp_rows):
        for j in range(1,dp_columns):
            if Input_list_wt[i-1] > j :
                dp[i][j] = dp[i-1][j]
            if Input_list_wt[i-1] <= j :
                dp[i][j] = min(dp[i-1][j] , 1 + dp[i][j - Input_list_wt[i-1]]  ) ## one has been added as coin has been considered

    print(dp)
    return dp[Input_list_len][Target]


def main():

    # Given a knapsack weight W and a set of n items with certain value vali and weight wti,
    # we need to calculate the maximum amount that could make up this quantity exactly
    input_list_wt = [9,6,5,1]
    Target_wt = 6

    Input_list_len = len(input_list_wt)
    Max_no_of_ways = Unbounded_knapsack_Coin_Change_Min_No_of_Coin(input_list_wt,Target_wt,Input_list_len)
    print(Min_no_of_ways)

if __name__ == "__main__" :
    main()