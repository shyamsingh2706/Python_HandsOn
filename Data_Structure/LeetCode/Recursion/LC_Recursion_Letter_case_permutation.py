# https://leetcode.com/problems/letter-case-permutation/

# Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.

# Example 1:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

# Example 2:
# Input: s = "3z4"
# Output: ["3z4","3Z4"]


def permutation_letter_case(arr,op='',output_arr=[]):

    if len(arr) == 0 :
        output_arr.append(op)
        return

    if arr[0].isdigit() == True:

        # if Digit , consider it as is given we dont have a choice in this scenario
        # reduce array size by 1 and call the recursion on remaining elements of array

        op1 = op
        op1 = op1 + arr[0]
        arr = arr[1:]
        permutation_letter_case(arr,op1,output_arr)

    else:

        # initilization in case the letter is not a digit
        op1 = op
        op2 = op

        # Considering first choice as Lower case and 2nd choice as upper case
        # concatenating in existing output as final output should be concatenated with this selection when it comes to end result
        op1 = op1 + arr[0].lower()
        op2 = op2 + arr[0].upper()

        # reduced the size of arr as first letter choice sepection has been done
        arr = arr[1:]

        # recursion call for next set of arr with similar choice recuresion tree dig
        permutation_letter_case(arr, op1, output_arr)
        permutation_letter_case(arr, op2, output_arr)

    return output_arr

def main():

    arr = "a1b2"
    print(permutation_letter_case(arr))

if __name__ == "__main__":
    main()