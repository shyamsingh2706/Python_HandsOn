
import numpy as np

# https://www.geeksforgeeks.org/printing-longest-common-subsequence/

# Given two sequences, print the longest subsequence present in both of them.

# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

def print_lcs(Input_list_X, Input_list_Y, Input_list_X_len, Input_list_Y_len ) :

    dp_rows = Input_list_X_len + 1
    dp_columns = Input_list_Y_len + 1

    dp = np.full((dp_rows,dp_columns),0).tolist()

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

    #print(dp)
    i = Input_list_X_len
    j = Input_list_Y_len

    # Following code is used to print LCS
    index = dp[Input_list_X_len][Input_list_Y_len]

    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]

    while ( i > 0 and j > 0) :

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if Input_list_X[i-1] == Input_list_Y[j-1]:
            lcs[index - 1] = Input_list_X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1

        else:
            j -= 1

    return "".join(lcs)


def main():


    X = "ABCDGH"
    Y = "AEDFHR"

    LCS = print_lcs(X,Y,len(X),len(Y))
    print("LCS for Input Sequence is : " , LCS)


if __name__ == "__main__":
    main()