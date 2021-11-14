# https://leetcode.com/problems/backspace-string-compare/

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack1 = []
        for ch in s:
            if ch == '#' and len(stack1) != 0:
                stack1.pop()
            elif ch != '#':
                stack1.append(ch)

        #print(stack1)
        stack2 = []
        for ch in t:
            if ch  == '#' and len(stack2) != 0:
                stack2.pop()
            elif ch  != '#':
                stack2.append(ch)

        #print(stack2)
        return stack1 == stack2

def main():
    a = "y#fo##f"
    b = "y#f#o##f"
    s = Solution()
    res = s.backspaceCompare(a,b)
    print(res)



if __name__ == "__main__":

    main()