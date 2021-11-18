# # https://leetcode.com/problems/jewels-and-stones/
# You're given strings jewels representing the types of stones that are jewels, and stones representing
# the stones you have. Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels_dict = collections.Counter(jewels)
        stones_dict = collections.Counter(stones)

        counter = 0

        for key in stones_dict.keys():

            if key in jewels_dict.keys():
                counter += stones_dict[key]

        return counter


def main():

    jewels = "aA"
    stones = "aAAbbbb"
    s = Solution()
    print(s.numJewelsInStones(jewels,stones))

if __name__ == "__main__":
    main()
