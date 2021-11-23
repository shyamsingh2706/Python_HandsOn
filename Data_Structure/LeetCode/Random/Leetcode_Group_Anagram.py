# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagram_dict = {}
        group_counter = 0
        res = {}
        for s in strs:

            # sort a given string and make it as a key of dictionary
            srt_s = ''.join(sorted(s))
            if srt_s in anagram_dict.keys():
                anagram_dict[srt_s].append(s)
            else:
                anagram_dict[srt_s] =[s]

        res =[]
        for i in anagram_dict.values():
            res.append(i)

        return res

def main():

    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    res = sol.groupAnagrams(strs)
    print(res)

if __name__ == "__main__":
    main()