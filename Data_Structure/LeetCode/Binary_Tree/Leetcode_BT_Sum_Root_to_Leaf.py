# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

# ✔️ Solution - I (Recursive DFS - Preorder)
# Time Complexity : O(N), where N is the number of nodes in the tree. We are doing a standard DFS traversal which takes O(N) time
# Space Complexity : O(H), where H is the maximum depth of tree.
# This space is required for implicit recursive stack space. In the worst case, the tree maybe skewed and H = N in which case space required is equal to O(N).


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = dfs(root, 0)
        return res

        def dfs(root, cur):
            if not root:
                return 0

            cur = cur * 10 + root.val
            if not root.left and not root.right:
                return cur
            return dfs(root.left, cur) + dfs(root.right, cur)

#  Solution - II (Iterative DFS - preorder)
# Time Complexity : O(N), where N is the number of nodes in the tree. We are doing a standard DFS traversal which takes O(N) time
# Space Complexity : O(H)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s, tot_sum = deque([(root, 0)]), 0
        while(len(s)):
            root, cur = s.pop()
            cur = cur * 10 + root.val
            if not root.left and not root.right:
                tot_sum += cur
            if root.right:
                s.append((root.right, cur))
            if root.left:
                s.append((root.left, cur))
        return tot_sum


