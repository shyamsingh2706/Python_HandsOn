import numpy as np

## https://www.geeksforgeeks.org/coin-change-dp-7/

def Unbounded_knapsack_Coin_Change_Max_Way (Input_list_wt,Target,Input_list_len):

    dp_rows = Input_list_len + 1
    dp_columns = Target + 1

    dp = np.full((dp_rows,dp_columns),0).tolist()


    for i in range(dp_rows):
        for j in range(dp_columns):
            if j == 0 :
                dp[i][j] = 1 ## Initialization will be 1 when J is 0 becuase  if target sum can be 0 with empty set only i.e. only one way possible
            elif i == 0 :
                dp[i][j] = 0 ## Initialization will be 0 when i is 0 because number of ways to get any sum is 0 with empty set

    #print(dp)

    for i in range(1,dp_rows):
        for j in range(1,dp_columns):
            if Input_list_wt[i-1] > j :
                dp[i][j] = dp[i-1][j]
            if Input_list_wt[i-1] <= j :
                dp[i][j] = (dp[i-1][j] + dp[i][j - Input_list_wt[i-1]] )

    return dp[Input_list_len][Target]


def main():

    # Given a knapsack weight W and a set of n items with certain value vali and weight wti,
    # we need to calculate the maximum amount that could make up this quantity exactly
    input_list_wt = [1,2,3]
    Target_wt = 4

    Input_list_len = len(input_list_wt)
    Max_no_of_ways = Unbounded_knapsack_Coin_Change_Max_Way(input_list_wt,Target_wt,Input_list_len)
    print(Max_no_of_ways)

if __name__ == "__main__" :
    main()