
## https://leetcode.com/problems/path-sum/

class TreeNode():

    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None


    def hasPathSum(self, root , targetSum) :

        if root is None:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)

        return left or right

def main() :

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    result = 22


    print("path sum with given value exists in given Tree, : " , root.hasPathSum(root,result))

if __name__ == "__main__" :
    main()

