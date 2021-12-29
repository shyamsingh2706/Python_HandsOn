# https://leetcode.com/problems/binary-tree-paths/

# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

class TreeNode():

    def __init__(self,val):
        self.val= val
        self.left = None
        self.right = None


    def binaryTreePaths(self, root) :

        paths = []
        if root is None:
            return paths

        self.dfs(root,'',paths)
        return paths

    def dfs(self,root,path,paths):

        # base condition
        path += str(root.val)
        if root.left is None and root.right is None:
            paths.append(path)
            return

        if root.left:
            self.dfs(root.left,path + '->' ,paths)

        if root.right:
            self.dfs(root.right,path + '->' ,paths)


def main() :

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)

    print("Sum of Left Leaves in given Tree, : " , root.binaryTreePaths(root))

if __name__ == "__main__" :
    main()