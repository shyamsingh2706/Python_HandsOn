# https://leetcode.com/problems/fizz-buzz/

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:

        res = []
        for idx in range(n):
            if (idx+1) % 5 == 0 and (idx+1) % 3 == 0:
                res.insert(idx,'FizzBuzz')
            elif (idx+1) % 3 == 0:
                res.insert(idx,'Fizz')
            elif (idx+1) % 5 == 0:
                res.insert(idx, 'Buzz')
            else:
                res.insert(idx, str(idx+1))

        return res

def main():
    n = 15
    s = Solution()
    print(s.fizzBuzz(n))

if __name__ == "__main__":
    main()

