# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ''
        for c in s:
            if c in ('a','e','i','o','u','A','E','I','O','U'):
                vowels += c

        vowels = vowels[::-1]
        s_new = ''
        counter = 0
        for c in s:
            if c in ('a','e','i','o','u','A','E','I','O','U'):
                s_new += vowels[counter]
                counter += 1
            else:
                s_new += c

        return s_new

    def reverseVowels_tuned(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        return "".join(s)

def main() :

    s = 'leetcode'
    S = Solution()
    res = S.reverseVowels_tuned(s)
    print(res)

if __name__ == "__main__":
    main()