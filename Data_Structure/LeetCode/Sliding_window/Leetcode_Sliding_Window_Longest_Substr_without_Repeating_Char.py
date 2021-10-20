import numpy as np

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

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

def lengthOfLongestSubstring_SW(arr) :

        start = 0
        end = 0

        Longest_Substr = 0

        temp_str = ''

        Longest_Substr = 0
        temp_substr = ''

        while end < len(arr):
            temp_substr = temp_substr + arr[end]
            # as we have to find all unique char, it intern means, it has be to be same as current window size
            # if length of uniqe substr chars are not same as window size and less than
            # it mean there are duplicate char
            if len(set(temp_substr)) < end - start + 1:
                # pop until Unique char length is same as current window size
                while len(set(temp_substr)) < end - start + 1:
                    temp_substr = temp_substr[1:]
                    start += 1
                end += 1
            # if number of unique char is same as window size then consider it as it might be candidate of longest substr
            if len(set(temp_substr)) == end - start + 1:
                Longest_Substr = max(Longest_Substr, end - start + 1)
                end += 1

        if Longest_Substr == 0:
            return -1
        else:
            return Longest_Substr


def main():
    arr = 'pwwkew'
    print("longest-substring-without-repeating-characters is ",  lengthOfLongestSubstring_SW(arr))


if __name__ == "__main__":
    main()

