# https://www.geeksforgeeks.org/longest-repeated-subsequence/

#Given a string, print the longest repeating subsequence such that the two subsequence don’t have same string character at same position,
#i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

# Input: str = "aabb"
# Output: 2 i.e."ab"

# Input: str = "aab"
# Output: 1 i.e. "a"
# The two subsequence are 'a'(first) and 'a'
# (second). Note that 'b' cannot be considered  as part of subsequence as it would be at same index in both.

# This problem is just the modification of Longest Common Subsequence problem.
# The idea is to find the LCS(str, str) where str is the input string with the restriction that when both the characters are same, they shouldn’t be on the same index in the two strings.


import numpy as np


def lcs_longest_repeated_subsequence (Input_list_X ,Input_list_Y,Input_list_X_len,Input_list_Y_len ) :


    dp_tab_rows = Input_list_X_len + 1
    dp_tab_columns = Input_list_Y_len + 1

    dp_tab = np.full((dp_tab_rows, dp_tab_columns),0).tolist()

    for i in range(dp_tab_rows):
        for j in range(dp_tab_columns):
            if ( i == 0 or j == 0 ) :
                dp_tab[i][j] = 0

    for i in range(1,dp_tab_rows):
        for j in range(1,dp_tab_columns):
            if ((Input_list_X[i-1] == Input_list_Y[j-1]) and ( i != j ) ) :
                dp_tab[i][j] = 1 + dp_tab[i-1][j-1]
            else:
                dp_tab[i][j] = max(dp_tab[i][j - 1] , dp_tab[i-1][j] )

    return dp_tab[Input_list_X_len][Input_list_Y_len]


def main():


    X = "AABEBCCD"
    Y = X

    LCS_Length = lcs_longest_repeated_subsequence(X,Y,len(X),len(Y))
    print("longest Repeated Sub Seq length is: " , LCS_Length)



if __name__ == "__main__":
    main()