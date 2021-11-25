# https://leetcode.com/problems/ransom-note/


# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magzine_dict = collections.Counter(magazine)

        for ch in ransomNote:

            if ch in magzine_dict.keys():
                if magzine_dict[ch] > 0:
                    magzine_dict[ch] -= 1

                if magzine_dict[ch] == 0:
                    del magzine_dict[ch]
            else:

                return False

        return True


def main():

    ransomNote = "a"
    magazine = "b"
    sol = Solution()
    print(sol.canConstruct(ransomNote,magazine))

if __name__ == "__main__":
    main()