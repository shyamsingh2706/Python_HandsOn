# https://leetcode.com/problems/binary-number-with-alternating-bits/
# Given a positive integer, check whether it has alternating bits:
# namely, if two adjacent bits will always have different values.


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        n_bit = list(str(bin(n)[2:]))

        for i in range(1 ,len(n_bit)):
            if not ( int(n_bit[i]) ^ int(n_bit[ i -1]) ):
                return False

        return True

def main():

    x = 5
    s = Solution()
    print(s.hasAlternatingBits(x))

if __name__ == "__main__":
    main()
