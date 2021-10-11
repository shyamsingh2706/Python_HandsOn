import numpy as np



### find max sum for a given Subset if target limit is defined
def SubSet_Sum_Recurrsion(Input_list,Target,Input_list_len):

        if (Input_list_len == 0 or Target == 0 ):
            return 0

        if Input_list[Input_list_len-1] > Target :
            return SubSet_Sum_Recurrsion(Input_list,Target,Input_list_len-1)
        elif Input_list[Input_list_len-1] <= Target :
            return  max ( Input_list[Input_list_len-1] + SubSet_Sum_Recurrsion(Input_list,Target - Input_list[Input_list_len-1],Input_list_len-1) , SubSet_Sum_Recurrsion(Input_list,Target,Input_list_len-1) )

# Refer below link for detailed explanation
# https://tanishqvyas069.medium.com/dynamic-programming-subset-sum-c386126621cd
# Find if sum of any Subset of a given array is equal to input target Sum : True or Flase
# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
### Through Kanpsack Memoization Approach .

def SubSet_Sum_DP_Memoization(Input_list,Target,Input_list_len,dp):

        if ( dp[Input_list_len][Target] is not None ) :
             return dp[Input_list_len][Target]

        # Fill the subset table in Top Down manner
        if Input_list[Input_list_len-1] > Target :
            dp[Input_list_len][Target] = SubSet_Sum_DP_Memoization(Input_list,Target,Input_list_len-1,dp)
        elif Input_list[Input_list_len-1] <= Target :
            dp[Input_list_len][Target] = ((SubSet_Sum_DP_Memoization(Input_list,Target - Input_list[Input_list_len-1],Input_list_len-1,dp) ) or ( SubSet_Sum_DP_Memoization(Input_list,Target,Input_list_len-1,dp) ))

        #print (dp)
        return dp[Input_list_len][Target]

### Subset Sum Problem if "Found a subset with given sum as True or False"
### Through Kanpsack Tabulation Approach .
### Find if sum of any Subset of a given array is equal to input target Sum : True or Flase
## https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
def SubSet_Sum_DP_Tabulation(Input_list,Target,Input_list_len):

            dp_columns = Target+1
            dp_rows = Input_list_len+1
            dp = np.full((dp_rows,dp_columns), False ).tolist()
            #print (dp)

            for i in range(dp_rows):
                for j in range(dp_columns):

                    # If sum is 0, then answer is true
                    if (j == 0):
                        dp[i][j] = True
                    # If sum is not 0 and set is empty,
                    # then answer is false
                    elif (i == 0):
                        dp[i][j] = False

            # Fill the subset table in bottom up manner
            for i in range(1,dp_rows):
                for j in range(1,dp_columns):
                    if Input_list[i - 1] > j:
                        dp[i][j] = dp[i - 1][j]
                    elif Input_list[i - 1] <= j:
                        dp[i][j] = ((dp[i - 1][j]) or (dp[i - 1][j - Input_list[i - 1]]))
            #print(dp)
            return dp[Input_list_len][Target]

def initialize_list(Input_numbers):

    input_list = []
    for j in Input_numbers.split(','):
        input_list.append(int(j))
    return input_list


def main():

    Input_numbers = input('Enter Your Input Array as "," seperated numbers : ' )
    target = int(input('Enter Your target Sum : '))

    #print(Input_numbers)
    #print(target)
    input_list = initialize_list(Input_numbers)
    Input_list_len = len(input_list)
    output_indices = SubSet_Sum_Recurrsion(input_list,target,Input_list_len)
    print(output_indices)
    if (SubSet_Sum_DP_Tabulation(input_list,target,Input_list_len) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")

    ### Intialization for Memoization Approach
    dp_columns = target + 1
    dp_rows = Input_list_len + 1
    dp = np.full((dp_rows, dp_columns), None).tolist()
    # print (dp)
    for i in range(dp_rows):
        for j in range(dp_columns):

            # If sum is 0, then answer is true
            if (j == 0):
                dp[i][j] = True
            # If sum is not 0 and set is empty,
            # then answer is false
            elif (i == 0):
                dp[i][j] = False

    if (SubSet_Sum_DP_Memoization(input_list,target,Input_list_len,dp) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")


if __name__ == "__main__":

    main()