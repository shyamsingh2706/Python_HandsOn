# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def ConstructBSTrecursive(self,nums,left,right):
        if left > right:
            return None
        mid = left + (right-left)//2
        current = TreeNode(nums[mid])
        current.left = self.ConstructBSTrecursive(nums,left,mid-1)
        current.right = self.ConstructBSTrecursive(nums, mid+1, right)

        return current

    def sortedArrayToBST(self, nums: list[int]):

        if len(nums) == 0 :
            return None

        return self.ConstructBSTrecursive(nums, 0, len(nums) -1 )



def main():

    nums = [-10,-3,0,5,9]
    s = Solution()
    res = s.sortedArrayToBST(nums)
    print(res)

if __name__ == "__main__":
    main()