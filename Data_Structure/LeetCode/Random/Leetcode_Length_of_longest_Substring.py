import numpy as np

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(input_list) -> int:
    if len(input_list) == 0:
        return 0

    res = []
    count = 0
    for ele in input_list:
        if ele in res:
            res = res[res.index(ele) + 1:]
        res.append(ele)
        count = max(count, len(res))
    return count


output = lengthOfLongestSubstring('pwwkew')
#output = lengthOfLongestSubstring('dvdf')
print(output)