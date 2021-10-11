import numpy as np

## https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
## As repetition allowed for a given item in Unbounded knapsack, input_list_len - 1 will be done only when we dont consider an item
## if we consider an item , we have to always consider the entire list. dp[i] ; for target weight, we need to consider its assciated value Input_list_val[i-1] and reduce the column target WT with the WT just considered i.e.  dp[i][j - Input_list_wt[i-1]]
## Thats the only difference between 0_1_knapsack vs unbounded_Knapsack

### knapsack 0_1 vs knapsack unbounded ( for Rod cutting problem )
#  wt array --> same as length arrray ( poosible devesions from a given length )
#  val --> Price  ( price of each sub length items )
#  W ( total target weight that need to be maximized ) --> N ( total target length of Rod )

def Unbounded_knapsack(Input_list_wt,Input_list_val,Target,Input_list_len):

    dp_rows = Input_list_len + 1
    dp_columns = Target + 1

    ## Initialization will be 0 when J is 0 becuase profile will always be 0 if input list is empty
    dp = np.full((dp_rows,dp_columns),0).tolist()
    #print(dp)

    for i in range(1,dp_rows):
        for j in range(1,dp_columns):
            if Input_list_wt[i-1] > j :
                dp[i][j] = dp[i-1][j]
            if Input_list_wt[i-1] <= j :
                dp[i][j] = max(dp[i-1][j] , Input_list_val[i-1] + dp[i][j - Input_list_wt[i-1]] )

    return dp[i][j]



def main():

    # Given a knapsack weight W and a set of n items with certain value vali and weight wti,
    # we need to calculate the maximum amount that could make up this quantity exactly
    input_list_wt = [1,50]
    input_list_val = [1,30]
    Target_wt = 100

    Input_list_len = len(input_list_val)
    Max_profit = Unbounded_knapsack(input_list_wt,input_list_val,Target_wt,Input_list_len)
    print(Max_profit)

if __name__ == "__main__" :
    main()