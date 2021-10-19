#https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1

#Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.
# Input:
# txt = forxxorfxdofr
# pat = for
# Output: 3
# Explanation: for, orf and ofr appears
# in the txt, hence answer is 3.

import collections

def count_of_anagrams(arr,pat):

    anagram_dict = collections.Counter(pat) ## create dictionary for Anagram

    start= 0
    end = 0
    window_size = len(pat)
    anagram_count = 0
    temp_str =''

    while end < len(arr):

        temp_str = temp_str + arr[end]

        if end - start +1 < window_size:
            end += 1
        elif end - start + 1 == window_size:
            temp_dict = collections.Counter(temp_str) ## create dictionary for temp string for a given window
            if temp_dict == anagram_dict :
                anagram_count = anagram_count + 1

            temp_str = temp_str[1:] # remove the first element from the temp string while moving window
            start += 1
            end += 1

    return anagram_count

## In Above Approach , we are transversing Map again and again thats increasing time complexity a lot
def count_of_anagrams_tuned(arr,pat):

    anagram_dict = collections.Counter(pat) ## create dictionary for Anagram
    count = len(anagram_dict)
    start= 0
    end = 0
    window_size = len(pat)
    anagram_count = 0
    temp_str =''

    while end < len(arr):

        ## if a char is part of searched anagram pattern
        ## reduce its count by 1 as its counted once
        ## if its counted fully, reduce overall count to 0
        if arr[end] in anagram_dict.keys():
            anagram_dict[arr[end]] = anagram_dict[arr[end]] - 1
            if anagram_dict[arr[end]] == 0:
                count = count - 1

        if end - start +1 < window_size:
            end += 1
        elif end - start + 1 == window_size:
            # if overall count is 0 , that means word found is anagram
            # increase anagram count by 1
            if count == 0  :
                anagram_count = anagram_count + 1

            # Before dropping first element of window
            # we have to increase the size of respective dict key ( reverse operation of above)
            # its becuase a new element will be added from next window
            # also if respective element count is 0 in dict
            # as we are adding an element, we have to add the overal count ( reverse of above Operation )
            if arr[start] in anagram_dict.keys():
                if anagram_dict[arr[start]] == 0:
                    count = count + 1
                anagram_dict[arr[start]] = anagram_dict[arr[start]] + 1

            start += 1
            end += 1

    return anagram_count

def main():

    txt = 'forxxorfxdofr'
    pat = 'for'
    print("Max Sum Subarray of size K  is " , count_of_anagrams_tuned(txt,pat))

if __name__ == "__main__":
    main()