# https://leetcode.com/problems/frog-jump/

# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.


import collections
class Solution:
    def canCross(self, stones: list[int]) -> bool:

        stonesMap = collections.Counter(stones)
        lastStone = stones[-1]

        # creating 2 statck to keep a track of position & respective Jump
        positions = []
        jumps = []

        positions.append(0)
        jumps.append(0)

        while positions :
            position = positions.pop()
            jump = jumps.pop()

            for i in range(jump-1,jump+2):
                if i <= 0 :
                    continue

                nextPos = position+i
                if nextPos == lastStone:
                    return True
                elif nextPos in stonesMap.keys():
                    positions.append(nextPos)
                    jumps.append(i)
                    continue

        return False

    def canCross_Optimized(self, stones: list[int]) -> bool:
        # no stones
        if not stones:
            return True

        stone_dict = {}
        for i in stones:
            stone_dict[i] = []

        # fist stone can only jump 1
        stone_dict[0] = [1]

        # no need the finally stone
        for i in stones:
            for j in (stone_dict[i]):
                # the j is one of the list [jump steps], s_key is next stone
                # s_key is stone + last jumps ( j , j-1 & j + 1 ) that make a possible next stone

                s_key = i + j
                # if next stone is presnt in dict
                if s_key in stone_dict:
                    # capture possible Jump values for each stone i.e. j-1,j & j + 1
                    if j not in stone_dict[s_key]:
                        stone_dict[s_key].append(j)
                    if j - 1 > 0 and j - 1 not in stone_dict[s_key]:
                        stone_dict[s_key].append(j - 1)
                    if j + 1 not in stone_dict[s_key]:
                        stone_dict[s_key].append(j + 1)
                        # if the stone_dict[stones[-1]] not [], can jump to it
        if stone_dict[stones[-1]]:
            return True
        else:
            return False

def main():

    stones = [0,1,3,5,6,8,12,17]

    sol = Solution()
    print(sol.canCross_Optimized(stones))

if __name__ == "__main__":
    main()