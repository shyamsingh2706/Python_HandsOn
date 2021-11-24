# https://leetcode.com/problems/count-primes/
# Given an integer n, return the number of prime numbers that are strictly less than n.


class Solution:
    def countPrimes(self, n: int) -> int:

        # create an array of Prime NUmbers assuming all numbers are Prime
        is_prime = [True] * n

        #iterate from index 2 as  0 & 1 are not a prime number
        for i in range(2, n):
            if is_prime[i]:
                # check for every multiple of i ( thats less that N ) and set it to Flase as they are not prime
                for j in range(i, n):
                    if j * i < n:
                        is_prime[i * j] = False
                    else:
                        break

        # count number of True left that will be prime numbers
        counter = 0
        for i in range(2, n):
            if is_prime[i] == True:
                counter += 1

        return counter

def main() :

    n = 10
    S = Solution()
    res = S.countPrimes(n)
    print(res)

if __name__ == "__main__":
    main()