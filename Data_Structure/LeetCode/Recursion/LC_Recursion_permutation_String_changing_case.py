#https://www.geeksforgeeks.org/permute-string-changing-case/

# Print all permutations of a string keeping the sequence but changing cases.
# Examples:

# Input : ab
# Output : AB Ab ab aB

# Input : ABC
# Output : abc Abc aBc ABc abC AbC aBC ABC

def permutation_changing_case(arr,op='',output_arr=[]):


    if len(arr) == 0 :
        output_arr.append(op)
        return

    # initilization
    op1 = op
    op2 = op

    # Considering first choice as Lower case and 2nd choice as upper case
    # concatenating in existing output as final output should be concatenated with this selection when it comes to end result
    op1 = op1 + arr[0].lower()
    op2 = op2 + arr[0].upper()

    # reduced the size of arr as first letter choice sepection has been done
    arr = arr[1:]

    # recursion call for next set of arr with similar choice recuresion tree dig
    permutation_changing_case(arr, op1, output_arr)
    permutation_changing_case(arr, op2, output_arr)

    return output_arr

def main():

    arr = "ab"
    print(permutation_changing_case(arr))

if __name__ == "__main__":
    main()