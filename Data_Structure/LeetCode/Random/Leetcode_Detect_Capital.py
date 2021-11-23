# https://leetcode.com/problems/detect-capital/
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 0:
            return False

        if len(word) == 1:
            return True

        while True:

            if word[0].isupper():

                if word[1].isupper():

                    while True:
                        word = word[1:]
                        if len(word) > 0 :
                            if not (word[0].isupper()):
                                return False
                        else:
                            return True

                elif word[1].islower():

                    while True:
                        word = word[1:]
                        if len(word) > 0:
                            if not (word[0].islower()):
                                return False
                        else:
                            return True

            else:

                while True:
                    word = word[1:]
                    if len(word) > 0:
                        if not (word[0].islower()):
                            return False
                    else:
                        return True

    def detectCapitalUse_tuned (self, word: str) -> bool:

        capital_count = 0
        for ch in word:
            if ch.isupper():
                capital_count += 1

        return capital_count == len(word) or capital_count == 0 or (capital_count == 1 and word[0].isupper())


def main():

    strs = 'USA'
    sol = Solution()
    res = sol.detectCapitalUse_tuned(strs)
    print(res)

if __name__ == "__main__":
    main()