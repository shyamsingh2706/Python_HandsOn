import numpy as np

# https://www.geeksforgeeks.org/longest-common-substring-dp-29/

def Longest_Common_Substring_recurssion(Input_list_X ,Input_list_Y , Input_list_X_len ,Input_list_Y_len, result ) :

    if ( Input_list_X_len ==0 or Input_list_Y_len == 0 ) :
        return result
    elif ( Input_list_X[Input_list_X_len-1] == Input_list_Y[Input_list_Y_len - 1]) :
         result =   Longest_Common_Substring_recurssion(Input_list_X ,Input_list_Y , Input_list_X_len-1 ,Input_list_Y_len-1 , result + 1 )
    else:
         result = max (result , max(Longest_Common_Substring_recurssion(Input_list_X, Input_list_Y, Input_list_X_len - 1, Input_list_Y_len, 0),
                   Longest_Common_Substring_recurssion(Input_list_X, Input_list_Y, Input_list_X_len, Input_list_Y_len - 1 , 0 )
                   ) )
    return result

def Longest_Common_Substring_Tabulation  (Input_list_X ,Input_list_Y , Input_list_X_len ,Input_list_Y_len ) :

    dp_rows = Input_list_X_len + 1
    dp_columns = Input_list_Y_len + 1

    dp = np.full((dp_rows,dp_columns),0).tolist()
    result = 0

    for i in range(dp_rows):
        for j in range(dp_columns):
            if i == 0 or j == 0 :
                dp[i][j] = 0

    for i in range(1,dp_rows) :
        for j in range(1,dp_columns):
            if Input_list_X[i-1] == Input_list_Y[j-1] :
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(result,dp[i][j])
            else:
                dp[i][j] = 0
    # we have to return the max value in the matrix and not t[m][n].
    # Just traverse through the matrix once and store max value in a variable and return that.
    # Why it is so? Cuz substring can exist anywhere in between.
    return result

def main():

    X = "OldSite:GeeksforGeeks.org"
    Y = "NewSite:GeeksQuiz.com"

    #X = "GeeksforGeeks"
    #Y = "GeeksQuiz"
    #LCS_Length = Longest_Common_Substring_recurssion(X,Y,len(X),len(Y),0)
    #print("Through Recurrsion : " , LCS_Length)

    LCS_Length_Tab = Longest_Common_Substring_Tabulation(X, Y,len(X),len(Y))
    print("Through Tabulation : " , LCS_Length_Tab)


if __name__ == "__main__":
    main()