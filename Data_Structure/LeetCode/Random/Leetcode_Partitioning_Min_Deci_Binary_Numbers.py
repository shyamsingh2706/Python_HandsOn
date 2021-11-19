# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
# For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
# Given a string n that represents a positive decimal integer,
# return the minimum number of positive deci-binary numbers needed so that they sum up to n.

class Solution:
    def minPartitions_BF(self, n: str) -> int:

        counter = 0
        while int(n) != 0 :

            LenStr = len(n)
            num = ''
            for i in range(LenStr):
                if n[i] == '0':
                    num = num + '0'
                else:
                    num = num + '1'

            n = str(int(n) - int(num))
            counter += 1


        return counter

    def minPartitions(self, n: str) -> int:
        # number of partitions will be same as max number present in string
        return int(max(n))

def main():

    n = "82734"
    s = Solution()
    print(s.minPartitions(n))

if __name__ == "__main__":
    main()