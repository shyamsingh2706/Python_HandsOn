import LCS_Basics_recurrsion_DP

# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
# https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/

# Given a sequence, find the length of the longest palindromic subsequence in it.

# The naive solution for this problem is to generate all subsequences of the given sequence and find the longest palindromic subsequence.
# This solution is exponential in term of time complexity.
# Let us see how this problem possesses both important properties of a Dynamic Programming (DP) Problem and can efficiently be solved using Dynamic Programming.

# If we reverse the existing string and find longest common sub sequence for both string , it will result into longest-palindromic-subsequence
# if the given sequence is “BBABCBCAB”, then the output should be 7 as “BABCBAB” is the longest palindromic subsequence in it.


def LCS_Longest_Palindrome_SebSeq ( Input_list_X , Input_list_Y ):

    Input_list_X_len = len(Input_list_X)
    Input_list_Y_len = len(Input_list_Y)

    long_plaindrome_sebSeq_len = LCS_Basics_recurrsion_DP.LCS_Tabulation(Input_list_X, Input_list_Y,Input_list_X_len,Input_list_Y_len)

    return long_plaindrome_sebSeq_len


def main() :

    X = "geeksforgeeks"
    Y = X[::-1]  ## Reverse String X

    long_plaindrome_sebSeq_len = LCS_Longest_Palindrome_SebSeq(X,Y)
    print("The length of the LPS is : ", long_plaindrome_sebSeq_len)

    print("Min No of Deletion to make an String Palindrome is : ", len(X) - long_plaindrome_sebSeq_len)
    ## Number of insertion will also be same as deletion as if elements that are getting deleted will be inserted in right order
    ## it will result into a palindrome string
    print("Min No of Insertion to make an String Palindrome is : ", len(X) - long_plaindrome_sebSeq_len)

if __name__ == "__main__":
    main()