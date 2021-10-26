# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def solve(parenthesis):
    stack = []
    open = ['(', '{', '[']
    close = [')', '}', ']']

    for ch in parenthesis:
        if ch in open:
            stack.append(close[open.index(ch)])

        elif len(stack) != 0 and ch == stack[-1]:
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


def main():
    arr = "{[]}"
    print("Valid Parentheses for given combination is ", solve(arr))


if __name__ == "__main__":
    main()