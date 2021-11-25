# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.


# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()
        self.res = []
        self.backtrack([], 0, target, candidates)

        return self.res

    def backtrack(self, cur_comb, cur_pos, target, candidates):

        if target == 0:
            self.res.append(cur_comb.copy())
        if target < 0:
            return

        prev = -1

        for i in range(cur_pos, len(candidates)):
            if candidates[i] == prev:  # to avoid repetition
                continue
            cur_comb.append(candidates[i])
            self.backtrack(cur_comb, i + 1, target - candidates[i], candidates)
            cur_comb.pop()  # for considering new combination
            prev = candidates[i]

def main():

    candidates  =  [10,1,2,7,6,1,5]
    target = 8
    sol = Solution()
    res = sol.combinationSum2(candidates,target)

    print(res)

if __name__ == "__main__":

    main()