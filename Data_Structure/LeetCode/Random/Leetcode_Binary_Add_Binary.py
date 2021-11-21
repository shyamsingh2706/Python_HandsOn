# https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = []
        carry = 0

        while len(a) != 0 and len(b) != 0:

            a_temp = int(a[-1])
            b_temp = int(b[-1])

            sum_temp = a_temp + b_temp + carry

            res.insert(0, str(sum_temp % 2))
            carry = sum_temp // 2

            a = a[:-1]
            b = b[:-1]

        while len(a) != 0:

            a_temp = int(a[-1]) + carry

            res.insert(0, str(a_temp % 2))
            carry = a_temp // 2

            a = a[:-1]

        while len(b) != 0:

            b_temp = int(b[-1]) + carry

            res.insert(0, str(b_temp % 2))
            carry = b_temp // 2

            b = b[:-1]

        if carry != 0:
            res.insert(0, str(carry))

        return ''.join(res)

def main():
    a = "11"
    b = "1"
    s = Solution()
    print(s.addBinary(a,b))

if __name__ == "__main__":
    main()