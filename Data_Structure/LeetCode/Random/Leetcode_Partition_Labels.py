# https://leetcode.com/problems/partition-labels/
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

import collections

class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        fre_dict = {}
        # Capture Index of each occurence for each element
        for i in range(len(s)):
            if s[i] in fre_dict.keys():
                fre_dict[s[i]].append(i)
            else:
                fre_dict[s[i]] = [i]

        res = []

        min_index = 0
        max_index = 0
        temp = 0
        counter = 0

        # loop through dict
        for key in fre_dict.keys():

            # set Min and Max index for a window in first ieration
            if counter == 0 :
                min_index = fre_dict[key][0]
                max_index = fre_dict[key][-1]
                counter += 1

            # if next element range is falling between existing min & max , continue
            elif fre_dict[key][0] > min_index and fre_dict[key][-1] < max_index:

                        continue

            # if next element start index is faling between existing Min & max but end index greater than max index
            # Then reset max index
            elif fre_dict[key][0] > min_index and fre_dict[key][0] < max_index and fre_dict[key][-1] > max_index:

                        max_index = fre_dict[key][-1]

            else:

                # if all above conditions are not met, means a new window can start
                # add existing window into result array
                res.append(max_index+1 - temp )
                temp = max_index+1

                # reset min & max index
                min_index = fre_dict[key][0]
                max_index = fre_dict[key][-1]

        # once all dict elements are browsed
        # add last window into result array i.e. final window's max index
        res.append(max_index + 1 - temp)

        return res

    def partitionLabels_TUNED(self, S):
        results = []
        last = {}

        for i in range(len(S) - 1, -1, -1):
            if S[i] not in last:
                last[S[i]] = i


        i = 0
        span = 0
        while i < len(S):
            j = last[S[i]]
            span = 1
            while i != j:
                i += 1
                span += 1
                j = max(j, last[S[i]])
            results.append(span)
            i += 1

        return results

def main():
    t = "caedbdedda"
    s = Solution()
    print(s.partitionLabels_TUNED(t))

if __name__ == "__main__":
    main()
