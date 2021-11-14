# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:

        reversed=0
        is_negative = 'N'
        if x < 0:
            is_negative ='Y'

        num = abs(x)
        while num > 0 :
            reversed = reversed*10 + num%10
            num = num // 10


        if reversed not in range(-2**31,2**31-1):
            return 0

        if is_negative == 'Y':
            return -1*reversed

        return reversed

def main():

    nums = 3211
    s = Solution()
    res = s.reverse(nums)
    print(res)



if __name__ == "__main__":

    main()