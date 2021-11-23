# https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if p is None and q is None:
            return True

        if not (p.val == q.val):
            return False

        if p.val == q.val and p.left is None and p.right is None and q.left is None and q.right is None:
            return True

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)