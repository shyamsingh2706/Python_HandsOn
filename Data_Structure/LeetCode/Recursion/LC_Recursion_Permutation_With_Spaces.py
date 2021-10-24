# https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1


# Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.
# The output should be printed in sorted increasing order of strings

# Input:
# S = "ABC"
# Output: (A B C)(A BC)(AB C)(ABC)
# Explanation:
# ABC
# AB C
# A BC
# A B C
# These are the possible combination of "ABC".

def permutation_with_Spaces(arr,op ='',output_arr = []):

    if len(arr) == 0 :
        output_arr.append(op)
        return

    op1 = op
    op2 = op

    # considering Next letter of sequence without space as first choice
    op1 = op1+ arr[0]
    # considering Next letter of sequence with space as 2nd choice
    op2 = op2 + ' ' + arr[0]

    # reduced the size of arr as first letter choice sepection has been done
    arr = arr[1:]

    # recursion call for next set of arr with similar choice recuresion tree dig
    permutation_with_Spaces(arr,op1,output_arr)
    permutation_with_Spaces(arr,op2,output_arr)

    return output_arr

def main():

    arr = "ABCD"

    # We dont have a choice for first letter as space wil come into picuter only pst 1st letter occurence
    # so take first letter in the op letter as is
    op = arr[0]
    arr = arr[1:]

    print(permutation_with_Spaces(arr,op))

if __name__ == "__main__":
    main()