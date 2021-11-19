# https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == '':
            return True

        res = ''
        for i in s:
            if i.isdigit() == True or i.isalpha() == True:
                res = res  + i

        return res.lower() == res[::-1].lower()

    def isPalindrome_2p(self, s: str) -> bool:

        start = 0
        end = len(s)-1

        while start <= end:

            print(s[start].lower())
            print(s[end].lower())
            print(s[start].lower() == s[end].lower())

            if (s[start].isdigit() == True or s[start].isalpha() == True) and (s[end].isdigit() == True or s[end].isalpha() == True ) :
                if s[start].lower() == s[end].lower() :
                    start += 1
                    end -= 1
                else:
                    return False
            elif not (s[start].isdigit() == True or s[start].isalpha() == True):
                start += 1
            elif not (s[end].isdigit() == True or s[end].isalpha() == True ) :
                end -= 1

        return True

def main():

    t = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.isPalindrome_2p(t))

if __name__ == "__main__":
    main()
