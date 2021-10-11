
import numpy as np

# https://www.geeksforgeeks.org/print-shortest-common-supersequence/

# Given two strings X and Y, print the shortest string that has both X and Y as subsequences.
# If multiple shortest supersequence exists, print any one of them.

# Examples:
# Input: X = "AGGTAB",  Y = "GXTXAYB"
# Output: "AGXGTXAYB" OR "AGGXTXAYB"


# We start from the bottom-right most cell of the matrix and
# push characters in output string based on below rules-

#  1. If the characters corresponding to current cell (i, j)
#     in X and Y are same, then the character is part of shortest
#     supersequence. We append it in output string and move
#     diagonally to next cell (i.e. (i - 1, j - 1)).

#  2. If the characters corresponding to current cell (i, j)
#     in X and Y are different, we have two choices -

#     If matrix[i - 1][j] > matrix[i][j - 1],
#     we add character corresponding to current
#     cell (i, j) in string X in output string
#     and move to the left cell i.e. (i, j - 1)
#     else
#     we add character corresponding to current
#     cell (i, j) in string Y in output string
#     and move to the top cell i.e. (i - 1, j)

#  3. If string Y reaches its end i.e. j = 0, we add remaining
#     characters of string X in the output string
#     else if string X reaches its end i.e. i = 0, we add
#     remaining characters of string Y in the output string.

def print_scs(Input_list_X, Input_list_Y, Input_list_X_len, Input_list_Y_len ) :

    dp_rows = Input_list_X_len + 1
    dp_columns = Input_list_Y_len + 1

    dp = np.full((dp_rows,dp_columns),0).tolist()

    ## Populate DP same as LCS
    for i in range(dp_rows):
        for j in range(dp_columns):
            if i == 0 or j == 0 :
                dp[i][j] = 0

    for i in range(1,dp_rows):
        for j in range(1,dp_columns):
            if Input_list_X[i-1] == Input_list_Y[j-1]:
                dp[i][j]=  1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    scs = ""

    i = Input_list_X_len
    j = Input_list_Y_len

    while ( i > 0 and j > 0 ) :
        # If current character in X and Y are same,
        # then current character is part of shortest supersequence and consider it only once
        if Input_list_X[i-1] == Input_list_Y[j-1] :
            scs += Input_list_X[i-1]
            i -= 1
            j -= 1
        # If current character in X and Y are different, still consider it as its super sequence
        # In LCS we need to ignore as its a sub sequence but in SCS we have to consider as its Super Sequence
        elif dp[i-1][j] > dp[i][j-1]:
            scs += Input_list_X[i-1]
            i -= 1
        else:
            scs += Input_list_Y[j-1]
            j -= 1

    # If X or Y reaches its end, put remaining characters of X or Y respectively in the result string

    while (i > 0):
        scs += Input_list_X[i - 1]
        i -= 1

    while (j > 0):
        scs += Input_list_Y[j - 1]
        j -= 1

    return scs[::-1]

def main():


    X = "HELLO"
    Y = "GEEK"

    SCS = print_scs(X,Y,len(X),len(Y))
    print("SCS for Input Sequence is : " , SCS)


if __name__ == "__main__":
    main()