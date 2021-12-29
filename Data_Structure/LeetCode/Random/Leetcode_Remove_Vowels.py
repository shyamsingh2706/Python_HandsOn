# https://leetcode.com/problems/remove-vowels-from-a-string/
# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

class Solution:
    def remove_vowels(self,char_str) :

        char_str = char_str.replace('a','' )
        char_str = char_str.replace('e','')
        char_str = char_str.replace('i','')
        char_str = char_str.replace('o','')
        char_str = char_str.replace('u','')

        return char_str

def main():

    str = 'leetcodeisacommunityforcoders'
    s = Solution()
    print(s.remove_vowels(str))

if __name__ == "__main__":
    main()