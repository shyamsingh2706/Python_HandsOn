# https://leetcode.com/problems/number-complement/

# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

class Solution:
    def findComplement(self, num: int) -> int:

        num = list(str(bin(num)[2:]))
        for i, x in enumerate(num):
            if x == "0":
                num[i] = "1"
            elif x == "1":
                num[i] = "0"
        return (int("".join(num), 2))


def main():

    x = 5
    s = Solution()
    print(s.findComplement(x))

if __name__ == "__main__":
    main()
