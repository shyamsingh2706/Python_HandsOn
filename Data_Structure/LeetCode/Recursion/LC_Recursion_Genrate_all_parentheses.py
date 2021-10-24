# https://www.interviewbit.com/problems/generate-all-parentheses-ii/
# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

# For example, given n = 3, a solution set is:
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Make sure the returned list of strings are sorted.


# similar problem details
# https://leetcode.com/problems/generate-parentheses/discuss/1527106/Clean-Python-Solution-(Self-Explained-With-Other-Similar-Problems)

def Genrate_all_Parentheses(open_paren,close_paren,op='',output_arr=[]) :

    # append output into final array when both open and clsoe parentheses are exhausted i.e. their respective count is 0
    # i.e. we are in leaf of  recursion decision tree
    if open_paren == 0 and close_paren == 0 :
        output_arr.append(op)
        return

    # we have to choice to consider Open Parentheses until Open parentheses count is greater than 0
    if open_paren != 0 :

        op1 = op
        op1 = op1 + '('
        Genrate_all_Parentheses(open_paren-1,close_paren,op1,output_arr)

    # we have to choice to consider close Parentheses until close parentheses count is greater than Open parentheses
    if open_paren < close_paren :

        op2 = op
        op2 = op2 + ')'
        Genrate_all_Parentheses(open_paren, close_paren-1, op2, output_arr)

    return output_arr

def main():

    n = 3
    open = n
    close = n
    print(Genrate_all_Parentheses(open,close))

if __name__ == "__main__":
    main()