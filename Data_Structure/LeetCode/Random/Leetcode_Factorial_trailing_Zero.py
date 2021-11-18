# https://leetcode.com/problems/factorial-trailing-zeroes/

# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0
        checker = 5
        last_ans = 0

        while (True):
            count += (n // checker)
            if (count == last_ans):
                break

            last_ans = count
            checker = checker * 5

        return count


def main() :

    n = 25
    s = Solution()
    res  = s.trailingZeroes(n)
    print ( " Number of trailing zero is : ", res)
if __name__ == "__main__":
    main()