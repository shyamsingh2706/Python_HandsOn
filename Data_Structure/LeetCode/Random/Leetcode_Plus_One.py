#https://leetcode.com/problems/plus-one/
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        if len(digits) == 0:
            return None

        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            num=0
            plus_one = []
            # convert array to Number
            for j in digits:
                num = num*10 + j

            # add 1 to existing number
            num = num + 1
            # convert number to array
            while num > 0 :
                plus_one.insert(0,num%10)
                num = num // 10

            # return array
            return plus_one

def main():

    nums = [1,2,9]
    s = Solution()
    res = s.plusOne(nums)
    print(res)



if __name__ == "__main__":

    main()