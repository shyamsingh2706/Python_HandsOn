# https://leetcode.com/problems/find-the-difference/
# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
import collections
def findTheDifference(s: str, t: str) -> str:

    s_dict = {}
    for ch in s:
        if ch in s_dict.keys():
            s_dict[ch] += 1
        else:
            s_dict[ch] = 1

    res = ''
    for ch in t:
        if ch not in s_dict.keys():
            res = res + ch
        elif s_dict[ch] > 0 :
            s_dict[ch] -= 1
        elif ch in s_dict.keys() and s_dict[ch] == 0:
            res = res + ch
            del s_dict[ch]

    for key in s_dict.keys():
        if s_dict[key] != 0:
            res = res + key

    return res

def main():

    s = "a"
    t = "aa"
    s = Solution()
    res = s.findTheDifference(s,t)
    print(res)

if __name__ == "__main__":
    main()