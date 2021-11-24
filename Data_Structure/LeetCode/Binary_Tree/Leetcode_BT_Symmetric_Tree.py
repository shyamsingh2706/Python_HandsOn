# https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        return self.isSymmetric_tree(root.left, root.right)

    def isSymmetric_tree(self, left, right):

        if left is None or right is None:
            return left == right

        if left.val != right.val:
            return False

        return self.isSymmetric_tree(left.left, right.right) and self.isSymmetric_tree(left.right, right.left)



