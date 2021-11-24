# https://leetcode.com/problems/happy-number/

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:
    # Starting with any positive integer, replace the number by the sum of the squares of its digits.
    # Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    # Those numbers for which this process ends in 1 are happy.
    # Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:

        counter = 1
        while True:

            LenN = len(str(n))
            totalSum = 0
            N = str(n)

            for i in range(LenN):
                num = int(N[i])
                totalSum = totalSum + (num * num)

            if totalSum == 1:
                return True

            elif len(str(totalSum)) == 1 and counter != 1:

                return False

            else:
                n = totalSum
                counter += 1



def main():

    n = 19
    sol = Solution()
    print(sol.isHappy(n))

if __name__ == "__main__":
    main()