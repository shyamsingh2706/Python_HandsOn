import LCS_Basics_recurrsion_DP

# https://www.geeksforgeeks.org/minimum-number-deletions-insertions-transform-one-string-another/
# Given two strings ‘str1’ and ‘str2’ of size m and n respectively.
# The task is to remove/delete and insert the minimum number of characters from/in str1 to transform it into str2.
# It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.

# Input :
# str1 = "heap", str2 = "pea"

# Output :
# Minimum Deletion = 2 and
# Minimum Insertion = 1

# Explanation:
# p and h deleted from heap
# Then, p is inserted at the beginning
# One thing to note, though p was required yet
# it was removed/deleted first from its position and
# then it is inserted to some other position.
# Thus, p contributes one to the deletion_count
# and one to the insertion_count.

# Algorithm:

# str1 and str2 be the given strings.
# m and n be their lengths respectively.
# len be the length of the longest common subsequence of str1 and str2
# minimum number of deletions minDel = m – len
# minimum number of Insertions minInsert = n – len

def LCS_Min_Del_And_Insert ( Input_list_X , Input_list_Y ):

    Input_list_X_len = len(Input_list_X)
    Input_list_Y_len = len(Input_list_Y)

    common_sebsequence_len = LCS_Basics_recurrsion_DP.LCS_Tabulation(Input_list_X, Input_list_Y,Input_list_X_len,Input_list_Y_len)

    LCS_Min_Del_Len = (Input_list_X_len) - common_sebsequence_len
    LCS_Min_Insert_Len = (Input_list_Y_len) - common_sebsequence_len

    print ("Minimum number of deletions = ",LCS_Min_Del_Len)
    print ("Minimum number of Insertions = ",LCS_Min_Insert_Len)

def main() :

    X = "geeksforgeeks"
    Y = "geeks"

    LCS_Min_Del_And_Insert(X,Y)



if __name__ == "__main__":
    main()