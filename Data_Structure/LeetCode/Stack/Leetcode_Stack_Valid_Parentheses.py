# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self,parenthesis):
        self.stack = []
        self.open = ['(', '{', '[']
        self.close = [')', '}', ']']


        if len(parenthesis) == 1 or len(parenthesis) % 2 != 0 :
            return False

        for ch in parenthesis:
            if ch in self.open:
                self.stack.append(self.close[self.open.index(ch)])
            elif len(self.stack) != 0 and ch == self.stack[-1]:
                    self.stack.pop()
            else:
                return False

        if len(self.stack) == 0:
            return True
        else:
            return False


def main():
    arr = "))"
    s = Solution()
    print("Valid Parentheses for given combination is ", s.isValid(arr))


if __name__ == "__main__":
    main()
