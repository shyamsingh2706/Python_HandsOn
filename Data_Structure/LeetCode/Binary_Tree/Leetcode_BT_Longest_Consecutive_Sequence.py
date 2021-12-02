# https://leetcode.ca/2016-09-23-298-Binary-Tree-Longest-Consecutive-Sequence/

# 298.Binary Tree Longest Consecutive Sequence
#  Given a binary tree, find the length of the longest consecutive sequence path.
#  The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
#  The longest consecutive path need to be from parent to child (cannot be the reverse).

#  For example,
#
#     1
#      \
#       3
#      / \
#     2   4
#          \
#           5
#  Longest consecutive sequence path is 3-4-5, so return 3.
#
#
#     2
#      \
#       3
#      /
#     2
#    /
#  1
#  Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


class TreeNode():

    def __init__(self,data):
        self.val= data
        self.left = None
        self.right = None

    def longestConsecutivepath(self,root):

        self.maxPath = 1
        self.findlongestConsecutivepath(root,0,0,self.maxPath)
        return self.maxPath

    def findlongestConsecutivepath(self,root,curr_path,target,maxPath):

        if root is None :

            return

        # if current value is same as Target , increment path by 1
        elif root.val == target:

            curr_path += 1

        else:
            # else reset path by 1
            curr_path = 1

        self.maxPath = max(self.maxPath,curr_path) # calculate max path everytime

        if root.right is not None:
            # set the target as current node's value + 1
            self.findlongestConsecutivepath(root.right,curr_path,root.val+1,self.maxPath)

        if root.left is not None:
            # set the target as current node's value + 1
            self.findlongestConsecutivepath(root.left, curr_path, root.val+1, self.maxPath)


def main() :

    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(1)

    print("Longest Consecutive path is : " , root.longestConsecutivepath(root))

if __name__ == "__main__" :
    main()

