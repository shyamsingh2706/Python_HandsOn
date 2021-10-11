# https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/

import numpy as np

def countWays_boolean_parenthesization_Recurrsion(S,i,j,is_true):

    ## Initialization

    if ( i > j ): # Empty String
        return 0
    if ( i == j ): # single string
        if is_true == 1 : # is we need to evaluate final Output as True
            if S[i] == 'T' :
                return 1
            else:
                return 0
        else:# is we need to evaluate final Output as False
            if S[i] == 'F':
                return 1
            else:
                return 0

    temp_ans = 0

    for k in range(i+1,j,2):

        left_true = countWays_boolean_parenthesization_Recurrsion(S,i,k-1,1)
        left_false = countWays_boolean_parenthesization_Recurrsion(S, i, k-1, 0)
        right_true = countWays_boolean_parenthesization_Recurrsion(S, k+1,j,1)
        right_false = countWays_boolean_parenthesization_Recurrsion(S, k+1,j,0)

        # Evaluate AND operation
        if S[k] == '&':
            if is_true == 1 :
                temp_ans = temp_ans + right_true*left_true
            else:
                temp_ans = temp_ans + right_true * left_false + left_false * right_false + right_false * left_true

        # Evaluate OR operation
        if S[k] == '|':
            if is_true == 1:
                temp_ans = temp_ans + right_true * left_false + right_true * left_true + right_false * left_true
            else:
                temp_ans = temp_ans +   left_false * right_false

        # Evaluate XOR operation
        if S[k] == '^':
            if is_true == 1:
                temp_ans = temp_ans + right_true * left_false +  right_false * left_true
            else:
                temp_ans = temp_ans +   left_false * right_false + right_true * left_true

    return temp_ans


def countWays_boolean_parenthesization_Memoization(S,i,j,is_true):

    ## Initialization

    if ( i > j ): # Empty String
        return 0
    if ( i == j ): # single string
        if is_true == 1 : # is we need to evaluate final Output as True
            if S[i] == 'T' :
                return 1
            else:
                return 0
        else:# is we need to evaluate final Output as False
            if S[i] == 'F':
                return 1
            else:
                return 0

    temp_ans = 0

    if (dp[i][j][is_true] != -1):
        return dp[i][j][is_true]

    for k in range(i+1,j,2):
        ## This can be further tuned is if we precheck dp[i][k - 1][1],dp[i][k - 1][0],dp[k+1][j][1],dp[k+1][j][0]
        ## and make function call only if this is not present in DP
        left_true = countWays_boolean_parenthesization_Memoization(S,i,k-1,1)
        left_false = countWays_boolean_parenthesization_Memoization(S, i, k-1, 0)
        right_true = countWays_boolean_parenthesization_Memoization(S, k+1,j,1)
        right_false = countWays_boolean_parenthesization_Memoization(S, k+1,j,0)

        # Evaluate AND operation
        if S[k] == '&':
            if is_true == 1 :
                temp_ans = temp_ans + right_true*left_true
            else:
                temp_ans = temp_ans + right_true * left_false + left_false * right_false + right_false * left_true

        # Evaluate OR operation
        if S[k] == '|':
            if is_true == 1:
                temp_ans = temp_ans + right_true * left_false + right_true * left_true + right_false * left_true
            else:
                temp_ans = temp_ans +   left_false * right_false

        # Evaluate XOR operation
        if S[k] == '^':
            if is_true == 1:
                temp_ans = temp_ans + right_true * left_false +  right_false * left_true
            else:
                temp_ans = temp_ans +   left_false * right_false + right_true * left_true

    dp[i][j][is_true] = temp_ans
    return dp[i][j][is_true]

def main():
    symbols = "TTFT"
    operators = "|&^"
    S = ""
    j=0

    ## form entire string that contains symbols & Operators i.e. T|T&F^T
    for i in range(len(symbols)):
        S = S + symbols[i]
        if (j < len(operators)):
            S = S + operators[j]
            j += 1

    # We obtain the string  T|T&F^T
    # so I should be 0 and J should be Len(arr) - 1 ( keeping array Index in mind )
    # so either K should vary from i to J-1 i.e. loop should be between i to K-1 and from K+1 to j
    # Also K value should be K= K+2 as we need to keep K only on Operator to evaluate an expression
    # thats why if K value is at kth Index, left block index will be until k-1 and right index will start from K+1
    i = 0
    j = len(S) -1

    # There are 4 ways
    # ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and
    # (T|((T&F)^T))
    print("Through Recurrsion : " , countWays_boolean_parenthesization_Recurrsion(S,i,j,1))

    global dp
    dp = np.full((len(S)+1,len(S)+1,2),-1).tolist()

    print("Through Memoization : " , countWays_boolean_parenthesization_Memoization(S, i, j, 1))

if __name__ == "__main__":
    main()