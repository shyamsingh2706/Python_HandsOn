
## https://leetcode.com/problems/path-sum/

class TreeNode():

    def __init__(self,val):
        self.val= val
        self.left = None
        self.right = None


    def pathSum(self, root , sum) :

        paths = []
        cur_path = []
        self.findpaths(root,sum,cur_path,paths)
        return paths

    def findpaths(self,root,sum,cur_path,paths):

        if root is None:
            return

        cur_path.append(root.val)
        if sum == root.val and  root.left is None and root.right is None :
            paths.append(cur_path)
            return

        self.findpaths(root.left, sum-root.val,list(cur_path),paths)
        self.findpaths(root.right, sum-root.val,list(cur_path),paths)

def main() :

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)


    result = 22


    print("path sum with given value exists in given Tree, : " , root.pathSum(root,result))

if __name__ == "__main__" :
    main()

