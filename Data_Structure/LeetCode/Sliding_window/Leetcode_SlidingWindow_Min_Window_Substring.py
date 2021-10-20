# https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.
# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
import collections


def Min_window_substr(arr,t):

    start = 0
    end = 0

    val_dict = collections.Counter(t)
    count = len(val_dict)
    temp_str = ''
    min_window_substr = ''

    while end < len(arr):

        ## if any char thats part of pattern string
        ## update the pattern dict and reduce count by 1 from overall count for a given char
        temp_str = temp_str + arr[end]
        if arr[end] in val_dict.keys():
            val_dict[arr[end]] = val_dict[arr[end]] - 1
            if val_dict[arr[end]] == 0:
                count = count - 1

        # if count if still greater than 0
        # that means all inscope pattern char are not navigated yet
        if count > 0 :
            end += 1
        # if all inscope pattern char are navigated that means count is 0
        elif count == 0 :

            # move the start pointer until the count is greater than 0 i.e. when start pointer is on a char thats part of given pattern
            # if a char is not part of given pattern , simply move the start pointer
            while count == 0  :

                #debug_char = arr[start]
                #debug_str = arr[start:end+1]

                # Perform reverse Operation i.e. if a char is part of pattern
                # increae the dict count and overall count by 1
                # capture the substring for this window length as this can be a candidate for min length substring
                if arr[start] in val_dict.keys():
                    if val_dict[arr[start]] == 0:
                        count = count + 1
                    val_dict[arr[start]] = val_dict[arr[start]] + 1
                    temp_str = arr[start:end+1]
                    start += 1

                    # if current substring is small in size then previous substring
                    # capture the same else ignore
                    if min_window_substr == '':
                        min_window_substr = temp_str
                    elif len(min_window_substr) > len(temp_str):
                        min_window_substr = temp_str

                else :
                    start += 1
            #print (temp_str)
            end += 1

    return min_window_substr


def main():

    s = 'ADOBECODEBANC'
    t = 'ABC'
    print("Minimum Window Substring is " , Min_window_substr(s,t))

if __name__ == "__main__":
    main()
