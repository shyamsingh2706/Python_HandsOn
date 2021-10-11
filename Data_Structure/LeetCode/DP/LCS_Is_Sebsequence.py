
import LCS_Basics_recurrsion_DP

# https://leetcode.com/problems/is-subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Without DP
def isSubsequence(s, t):
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i+1:]
    return True

def LCS_is_SubSequence ( Input_list_X , Input_list_Y ):

    Input_list_X_len = len(Input_list_X)
    Input_list_Y_len = len(Input_list_Y)

    common_sebsequence_len = LCS_Basics_recurrsion_DP.LCS_Tabulation(Input_list_X, Input_list_Y,Input_list_X_len,Input_list_Y_len)

    if  (Input_list_X_len == common_sebsequence_len) or ( Input_list_Y_len == common_sebsequence_len ) :
        return True
    else:
        return False

def isSubsequence_stack(s: str, t: str) -> bool:

    stack = [ch for ch in s][::-1]

    for ch in t:
        if stack:
            if ch == stack[-1]:
                stack.pop()
        else:
            return True

    return not stack

def main() :

    X = "axc"
    Y = "ahxbgdc"

    # benifit of DP is , its dynamic and Input sequnce wont matter.
    # for other appraoch , Input Sequence do matter
    is_subSequence = LCS_is_SubSequence(X,Y)
    print(is_subSequence)



if __name__ == "__main__":
    main()