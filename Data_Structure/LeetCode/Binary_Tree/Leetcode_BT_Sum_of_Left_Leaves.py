# https://leetcode.com/problems/sum-of-left-leaves/

# Given the root of a binary tree, return the sum of all left leaves.

class TreeNode():

    def __init__(self,val):
        self.val= val
        self.left = None
        self.right = None


    def sumOfLeftLeaves(self, root) -> int:

        if root is None:
            return 0

        if root.left is not None and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)


def main() :

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Sum of Left Leaves in given Tree, : " , root.sumOfLeftLeaves(root))

if __name__ == "__main__" :
    main()