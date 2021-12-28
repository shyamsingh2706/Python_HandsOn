
# https://leetcode.com/problems/binary-tree-right-side-view
# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.


# Definition for a binary tree node.
class TreeNode():

    def __init__(self, data=None):

        self.val = data
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root) :

        if root is None:
            return

        tree = []
        result = []

        tree.append(root)
        length = 1

        while length:

            length = len(tree)
            for i in range(length):

                node = tree.pop(0)

                if i == length - 1:
                    result.append(node.val)

                if node.left:
                    tree.append(node.left)

                if node.right:
                    tree.append(node.right)

        return result


def main() :

    root = TreeNode(1)
    root.right = TreeNode(2)
    s= Solution()
    print(s.rightSideView(root))

if __name__ == "__main__":
    main()