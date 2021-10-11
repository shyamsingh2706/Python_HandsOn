
## https://leetcode.com/problems/diameter-of-binary-tree
## https://www.geeksforgeeks.org/diameter-of-a-binary-tree-in-on-a-new-method/

class BT():

    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None
        self.result = 0

    # just to cross validate binary tree order
    def Inorder_Traversal(self, root):
        # Inorder traversal
        # Left -> Root -> Right
        res = []
        if root:
            res = self.Inorder_Traversal(root.left)
            res.append(root.data)
            res = res + self.Inorder_Traversal(root.right)

        return res

    def diameter(self,root):

        if root == None:
            return 0

        left_height = self.diameter(root.left)
        right_height = self.diameter(root.right)

        ##  max Diameter of right and left tree if a given Node is not part of diameter
        ## So result has to be passed to parent node for further calculation
        ## + 1 has been added to consider self count before passing on further to parent
        temp = 1 + max(left_height,right_height)

        ## If individual node itself is part of diameter
        ## so Left + Right + 1 is diameter
        ## select max from temp and self diameter to pick maximum diameter
        ans = max(temp,(1+left_height+right_height))

        ## Decide max path among all possibilites of path among different nodes
        self.result = max(ans,self.result)

        # Return temp as if its a recursive call , we need result to be passed on to parent node
        ## Due to vary same reason , self.result is passed as reference to avoid it being modified as part of recursive call
        return temp


def main() :

    root = BT(1)
    root.left = BT(2)
    root.right = BT(3)
    root.left.left = BT(4)
    root.left.right = BT(5)

    result = 0
    #print("Diameter is", root.Inorder_Traversal(root))

    root.diameter(root)
    print("Diameter is : " , root.result)

if __name__ == "__main__" :
    main()