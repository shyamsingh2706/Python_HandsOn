# https://leetcode.com/problems/valid-palindrome-ii/
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true


class Solution:
    def validPalindrome_BF(self, s: str) -> bool:

        for i in range(len(s)):

            temp_str = s[:i] + s[i+1:]
            if temp_str == temp_str[::-1]:
                return True

        return False

    def validPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1
        counter = 0

        while start < end:

            # if start & end index char is not matching
            if s[start] != s[end]:

                # if its first encounter
                if counter == 0:

                    counter += 1

                    # check if string is palindrome if we skip start index char
                    # if yes, move start pointer
                    if self.is_palindrome(s[:start] + s[start + 1:]):
                        start += 1

                    # check if string is palindrome if we skip end index char
                    # if yes, move end pointer
                    elif self.is_palindrome(s[:end] + s[end + 1:]):
                        end -= 1

                    # if both are false
                    # return False
                    else:
                        return False

                # return Flase if its not first Encounter
                else:

                    return False

            start += 1
            end -= 1

        return True

    def is_palindrome(self, s):

        if s == s[::-1]:

            return True

        else:

            return False



def main():

    t = "eedede"
    s = Solution()
    print(s.validPalindrome(t))

if __name__ == "__main__":
    main()
