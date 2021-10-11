import numpy as np

## https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
## As repetition allowed for a given item in Unbounded knapsack, input_list_len - 1 will be done only when we dont consider an item
## if we consider an item , we have to always consider the entire list. dp[i] ; for target weight, we need to consider its assciated value Input_list_val[i-1] and reduce the column target WT with the WT just considered i.e.  dp[i][j - Input_list_wt[i-1]]
## Thats the only difference between 0_1_knapsack vs unbounded_Knapsack

### knapsack 0_1 vs knapsack unbounded ( for Rod cutting problem )
#  wt array --> same as length arrray ( poosible devesions from a given length )
#  val array --> same as Price array ( price of each sub length items )
#  W ( total target weight that need to be maximized for knapsack ) --> N ( total target length of Rod ) ( can be given or if not given will be same as Input list length )

def Unbounded_knapsack(Input_list_wt,Input_list_val,Target,Input_list_len):

    dp_rows = Input_list_len + 1
    dp_columns = Target + 1

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

    # Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n.
    # Determine the maximum value obtainable by cutting up the rod and selling the pieces
    input_list_wt = [1,2,3,4,5,6,7,8]
    input_list_val = [3,5,8,9,10,17,17,20]


    Input_list_len = len(input_list_val)
    Target = Input_list_len ### As Target Length is not given , we need to consider the Input list length as Target length

    Max_profit = Unbounded_knapsack(input_list_wt,input_list_val,Target_wt,Input_list_len)
    print(Max_profit)

if __name__ == "__main__" :
    main()