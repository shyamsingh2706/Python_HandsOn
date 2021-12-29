# https://leetcode.com/problems/repeated-dna-sequences/
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule. You may return the answer in any order.

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        result = set()
        for i in range(len(s)):
            str1 = s[i:i+10]
            str2 = s[i+1:]

            #print(str1 , str2)
            if str1 in str2:
                result.add(str1)

        return list(result)

    def findRepeatedDnaSequences_Optimized(self, s: str) -> list[str]:

        result = set()
        seen = set()
        for i in range(len(s)-9):
            str1 = s[i:i+10]
            #str2 = s[i+1:]
            #print(str1 , str2)
            if str1 in seen:
                result.add(str1)
            seen.add(str1)

        return list(result)

def main() :

    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    S = Solution()
    res = S.findRepeatedDnaSequences_Optimized(s)
    print(res)

if __name__ == "__main__":
    main()