import LCS_Basics_recurrsion_DP

# https://www.geeksforgeeks.org/shortest-common-supersequence/
# Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 and str2 as subsequences.

#Input:   str1 = "geek",  str2 = "eke"
#Output: 5
#Explanation:
#String "geeke" has both string "geek" and "eke" as subsequences.

# Solution Explanation:
# We need to find a string that has both strings as subsequences and is shortest such string.
# If both strings have all characters different, then result is sum of lengths of two given strings.
# If there are common characters, then we don’t want them multiple times as the task is to minimize length.
# Therefore, we first find the longest common subsequence, take one occurrence of this subsequence and add extra characters.
# Length of the shortest supersequence   = (Sum of lengths of given two strings)  - (Length of common LCS of two given strings)



def LCS_shortest_common_supersequence ( Input_list_X , Input_list_Y ):

    Input_list_X_len = len(Input_list_X)
    Input_list_Y_len = len(Input_list_Y)

    common_sebsequence_len = LCS_Basics_recurrsion_DP.LCS_Tabulation(Input_list_X, Input_list_Y,Input_list_X_len,Input_list_Y_len)

    shrt_common_super_seq_len = (Input_list_X_len+Input_list_Y_len) - common_sebsequence_len

    return shrt_common_super_seq_len

def main() :

    X = "geek"
    Y = "eke"

    shrt_common_super_seq_len = LCS_shortest_common_supersequence(X,Y)
    print("Length of the shortest supersequence is : ",shrt_common_super_seq_len)


if __name__ == "__main__":
    main()