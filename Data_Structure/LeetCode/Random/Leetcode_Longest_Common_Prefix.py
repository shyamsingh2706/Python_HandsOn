# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ''

        if len(strs) == 0 :

            return prefix

        index = 0
        for ch in strs[0]:
            for i in range(1,len(strs)):
                # if out of bound for a given string or its not matching with next string's char for same index position
                if index >= len(strs[i]) or ch != strs[i][index] :
                    return prefix

            prefix = prefix + ch
            index += 1
        return prefix


def main():

    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))

if __name__ == "__main__":
    main()
