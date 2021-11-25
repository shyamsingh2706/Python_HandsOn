# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()
        self.res = []
        self.backtrack([], 0, target, candidates)

        return self.res

    def backtrack(self, cur_comb, cur_pos, target, candidates):

        if target == 0:
            self.res.append(cur_comb.copy())
        if target < 0:
            return

        for i in range(cur_pos, len(candidates)):
            cur_comb.append(candidates[i])
            self.backtrack(cur_comb, i, target - candidates[i], candidates)
            cur_comb.pop()  # for considering new combination


def main():

    candidates  =  [2,3,6,7]
    target = 7
    sol = Solution()
    res = sol.combinationSum(candidates,target)

    print(res)

if __name__ == "__main__":

    main()