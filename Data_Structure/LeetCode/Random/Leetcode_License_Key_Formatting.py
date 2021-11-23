# https://leetcode.com/problems/license-key-formatting/

# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group,
# which could be shorter than k but still must contain at least one character.
# Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.

# Example 1:
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.replace('-','').upper()
        counter = 0
        res =[]

        for ch in s[::-1]:
            if counter == k :
                res.insert(0, '-')
                counter = 0
            res.insert(0, ch)
            counter += 1

        return ''.join(res)

def main():
    s = "2-5g-3-J"
    k = 2
    sol = Solution()
    res = sol.licenseKeyFormatting(s,k)
    print(res)

if __name__ == "__main__":
    main()