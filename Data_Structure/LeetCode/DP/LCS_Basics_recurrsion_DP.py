import numpy as np

## largest Common Sebsequence
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

# LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

def LCS_Recurssion (Input_list_X ,Input_list_Y , Input_list_X_len ,Input_list_Y_len ) :

    if ( Input_list_X_len == 0 or Input_list_Y_len == 0 ) :
        return 0

    elif (Input_list_X[Input_list_X_len-1] == Input_list_Y[Input_list_Y_len-1]) :
        return 1 + LCS_Recurssion(Input_list_X ,Input_list_Y , Input_list_X_len-1 ,Input_list_Y_len-1)

    else:
        return max ( LCS_Recurssion(Input_list_X ,Input_list_Y , Input_list_X_len-1 ,Input_list_Y_len)  ,
                     LCS_Recurssion(Input_list_X ,Input_list_Y , Input_list_X_len ,Input_list_Y_len -1)
                    )

def LCS_Tabulation (Input_list_X ,Input_list_Y,Input_list_X_len,Input_list_Y_len ) :


    dp_tab_rows = Input_list_X_len + 1
    dp_tab_columns = Input_list_Y_len + 1

    dp_tab = np.full((dp_tab_rows, dp_tab_columns),0).tolist()

    for i in range(dp_tab_rows):
        for j in range(dp_tab_columns):
            if ( i == 0 or j == 0 ) :
                dp_tab[i][j] = 0

    for i in range(1,dp_tab_rows):
        for j in range(1,dp_tab_columns):
            if (Input_list_X[i-1] == Input_list_Y[j-1]) :
                dp_tab[i][j] = 1 + dp_tab[i-1][j-1]
            else:
                dp_tab[i][j] = max(dp_tab[i][j - 1] , dp_tab[i-1][j] )

    return dp_tab[Input_list_X_len][Input_list_Y_len]


# https://www.geeksforgeeks.org/longest-common-subsequence-dp-using-memoization/
def LCS_Memoization (Input_list_X ,Input_list_Y , Input_list_X_len ,Input_list_Y_len ) :

    if ( Input_list_X_len == 0 or Input_list_Y_len == 0 ) :
        return 0

    elif dp_mem[Input_list_X_len][Input_list_Y_len] != - 1 :
        return dp_mem[Input_list_X_len][Input_list_Y_len]

    elif (Input_list_X[Input_list_X_len-1] == Input_list_Y[Input_list_Y_len-1]) :
        dp_mem[Input_list_X_len][Input_list_Y_len] = 1 + LCS_Memoization(Input_list_X ,Input_list_Y , Input_list_X_len-1 ,Input_list_Y_len-1 )

    else:
        dp_mem[Input_list_X_len][Input_list_Y_len] = max ( LCS_Memoization(Input_list_X ,Input_list_Y , Input_list_X_len-1 ,Input_list_Y_len )  ,  LCS_Memoization(Input_list_X ,Input_list_Y , Input_list_X_len ,Input_list_Y_len-1 ) )

    return dp_mem[Input_list_X_len][Input_list_Y_len]


def main():


    X = "AGGTAB"
    Y = "GXTXAYB"

    LCS_Length = LCS_Recurssion(X,Y,len(X),len(Y))
    print("Through Recurrsion : " , LCS_Length)

    LCS_Length_Tab = LCS_Tabulation(X, Y,len(X),len(Y))
    print("Through Tabulation : " , LCS_Length_Tab)

    # Memoization create and Initialize Matrix

    dp_mem_rows = len(X) + 1
    dp_mem_columns = len(Y) + 1

    global dp_mem
    dp_mem = np.full((dp_mem_rows,dp_mem_columns),-1).tolist()

    #print(dp_mem)
    for i in range(dp_mem_rows):
        for j in range(dp_mem_columns):
            if j == 0 :
                dp_mem[i][j] = 0
            if i == 0 :
                dp_mem[i][j] = 0

    #print(dp_mem)
    LCS_Length_Mem = LCS_Memoization(X, Y, len(X), len(Y) )
    print("Through Memoization : " , LCS_Length_Mem)




if __name__ == "__main__":
    main()