# https://practice.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1
# https://leetcode.com/discuss/interview-question/1517199/print-n-bit-binary-numbers-having-more-1s-than-0s-java-recursion

# Print N-bit binary numbers having more 1s than 0s

# Given a positive integer N, the task is to find all the N bit binary numbers having more than or equal 1’s than 0’s for any prefix of the number.
# Input:  N = 2
# Output: 11 10
# Explanation: 11 and 10 have more than
# or equal 1's than 0's

# Time: O(2^N), since we can roughly see every position has two options, open or close.
# Space: O(N) for recursion depth.

def generate_binary(n,No_of_one,No_of_zero,op='',output_arr=[]) :

    # append output into final array when all 1s and 0s are exhausted i.e. N = 0
    # i.e. we are in leaf of  recursion decision tree
    if n == 0 :
        output_arr.append(op)
        return

    # we have to choice to consider 1 throughout until N is 0
    if n != 0 :

        op1 = op
        op1 = op1 + '1'
        generate_binary(n-1,No_of_one+1,No_of_zero,op1,output_arr)

    # we have to choice to consider 0 until its less than 1's count
    if No_of_zero < No_of_one :

        op2 = op
        op2 = op2 + '0'
        generate_binary(n-1,No_of_one, No_of_zero+1, op2, output_arr)

    return output_arr

def main():

    n = 4
    No_of_one = 0
    No_of_zero = 0

    print(generate_binary(n,No_of_one,No_of_zero))

if __name__ == "__main__":
    main()