
## https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/

class Node():

    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None
        self.result = 0

    def Max_path_Sum(self,root):

        if root == None:
            return 0

        left_path_sum = self.Max_path_Sum(root.left)
        right_path_sum = self.Max_path_Sum(root.right)

        ##  max path sum of right and left tree will be picked if a given Node is not part of max path sum
        ##  as option is to start with leaf node only, existing node wil not have a choice to consider itself in case of negative weight.
        ##  so max condition that was present in any node to any node path sum can not be used here in case of leaf node to lead node
        ##  So result has to be passed to parent node for further calculation
        ##  root.data has been added to consider self weight before passing on further to parent
        temp = (root.data + max(left_path_sum,right_path_sum))

        ## If individual node itself is part of diameter
        ## so Left + Right + root.data is path sum
        ## select max from temp and self calculated sum to pick maximum path sum
        ans = max(temp,(root.data+right_path_sum+left_path_sum))

        ## Decide max path sum among all possibilites of path among different nodes
        self.result = max(ans,self.result)

        # Return temp as if its a recursive call , we need result to be passed on to parent node
        ## Due to vary same reason , self.result is passed as reference to avoid it being modified as part of recursive call
        return temp


def main() :

    root = Node(15)
    root.left = Node(5)
    root.right = Node(-6)
    root.left.left = Node(-8)
    root.left.right = Node(-1)
    root.right.left = Node(3)
    root.right.right = Node(9)

    result = 0
    #print("Diameter is", root.Inorder_Traversal(root))

    root.Max_path_Sum(root)
    print("Max Path Sum from any node to any node is : " , root.result)

if __name__ == "__main__" :
    main()

