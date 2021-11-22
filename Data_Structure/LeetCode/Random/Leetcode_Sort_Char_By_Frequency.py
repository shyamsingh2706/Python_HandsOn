# https://leetcode.com/problems/sort-characters-by-frequency/
# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


import collections
class Solution:
    def frequencySort(self, s: str) -> str:

        freq_dict = collections.Counter(s)
        print(freq_dict)
        freq_dict_sorted = sorted(freq_dict, key=freq_dict.get, reverse=True)
        print(freq_dict_sorted)
        res = ''

        for i in freq_dict_sorted:
            for j in range(freq_dict[i]):
                res = res + i

        return res

def main():

    s = 'tree'

    sol = Solution()
    print(sol.frequencySort(s))

if __name__ == "__main__":
    main()