#https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

# Given a string you need to print the size of the longest possible substring that has exactly K unique characters.
# If there is no possible substring then print -1.

# Input:
# S = "aabacbebebe", K = 3
# Output: 7
# Explanation: "cbebebe" is the longest substring with K distinct characters.

# Input:
# S = "aaaa", K = 2
# Output: -1
# Explanation: There's no substring with K distinct characters.


def largest_substr_K_Uniq_Char(arr,k):

    start = 0
    end = 0

    Longest_Substr = 0
    temp_substr = ''

    while end < len(arr):
        temp_substr = temp_substr + arr[end]

        if len(set(temp_substr)) < k :
            end += 1
        elif len(set(temp_substr)) == k :
            Longest_Substr = max(Longest_Substr,end-start+1)
            end += 1
        elif len(set(temp_substr)) > k :
            while len(set(temp_substr)) > k :
                temp_substr = temp_substr[1:]
                start +=1

            end +=1

    if Longest_Substr == 0:
        return -1
    else:
        return  Longest_Substr


def main():

    arr = 'aabacbebebe'
    k = 3
    print("Longest Substring With K Unique Characters is " , largest_substr_K_Uniq_Char(arr,k))

if __name__ == "__main__":
    main()



