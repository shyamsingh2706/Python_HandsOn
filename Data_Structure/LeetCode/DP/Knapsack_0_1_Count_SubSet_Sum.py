import Knapsack_0_1_SubSet_Sum
import numpy as np

#https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/
#Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.

def Kanpsack_0_1_Count_SubSet_Sum(Input_list,Target,Input_list_len):

    ### Initialize DP matrix to 0
    ### Where we have false initialize in subset sum , means subset cant be formed. Replace flase with 0
    ### Where we have True in Initialize Sub set sum, means one unique empty subset can be formed , Replace True with 1
    dp_columns = Target + 1
    dp_rows = Input_list_len + 1
    dp = np.full((dp_rows, dp_columns), 0).tolist()
    #print (dp)

    for i in range(dp_rows):
        for j in range(dp_columns):

            # If sum is 0, then answer is true
            if (j == 0):
                dp[i][j] = 1
            # If sum is not 0 and set is empty,
            # then answer is false
            elif (i == 0):
                dp[i][j] = 0

    #print(dp)

    for i in range(1,dp_rows):
        for j in range(1,dp_columns):
            if Input_list[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            elif Input_list[i - 1] <= j:
                dp[i][j] = ((dp[i - 1][j]) + (dp[i - 1][j - Input_list[i - 1]]))

    #print(dp)
    return dp[Input_list_len][Target]


def main():

    Input_numbers = input('Enter Your Input Array as list of "," seperated numbers : ' )
    target = int(input('Enter Your target Sum : '))

    input_list = Knapsack_0_1_SubSet_Sum.initialize_list(Input_numbers)
    Input_list_len = len(input_list)

    subset_count = Kanpsack_0_1_Count_SubSet_Sum(input_list,target,Input_list_len)
    print(subset_count)

if __name__ == "__main__" :
    main()