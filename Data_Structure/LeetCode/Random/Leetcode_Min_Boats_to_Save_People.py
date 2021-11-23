# https://leetcode.com/problems/boats-to-save-people/
# You are given an array people where people[i] is the weight of the ith person,
# and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.

import numpy as np
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        # sort people so that we know we have listest to heviest person details with us
        people = sorted(people)
        num_boats = 0

        start = 0
        end = len(people)-1

        while start <= end:
            # try to match lightest and heaviest toghether
            # if it wont work out, we have to consider heaviest person only
            if people[start] + people[end] <= limit:
                # if both work out, change the pointer
                start += 1
                end -= 1
            else:
                # if not, as we considered heaviest person. move the end pointer only
                end -= 1


            num_boats += 1

        return num_boats


def main() :

    arr = [1,2]
    limit = 3
    s = Solution()
    res  = s.numRescueBoats(arr,limit)
    print ( "Min Boat is  : ", res)

if __name__ == "__main__" :
    main()
