class BST_NODE():

    def __init__(self, data=None):

        self.data = data
        self.LeftChild = None
        self.RightChild = None

    def insert_node(self, data):

        if (self.data == data):
            return
        else:
            if data > self.data:
                if self.RightChild:
                    self.RightChild.insert_node(data)
                else:
                    self.RightChild = BST_NODE(data)
            elif data < self.data:
                if self.LeftChild:
                    self.LeftChild.insert_node(data)
                else:
                    self.LeftChild = BST_NODE(data)



    def Inorder_Traversal(self, root):
        # Inorder traversal
        # Left -> Root -> Right
        res = []
        if root:
            res = self.Inorder_Traversal(root.LeftChild)
            res.append(root.data)
            res = res + self.Inorder_Traversal(root.RightChild)
        return res

    def Preorder_Traversal(self, root):
        # Preorder traversal
        # Root -> Left ->Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.Inorder_Traversal(root.LeftChild)
            res = res + self.Inorder_Traversal(root.RightChild)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.LeftChild)
            res = res + self.PostorderTraversal(root.RightChild)
            res.append(root.data)
        return res


if __name__ == "__main__":

    Root = BST_NODE(3)
    Root.insert_node(4)
    Root.insert_node(1)
    Root.insert_node(2)
    Root.insert_node(5)
    Root.insert_node(6)
    print(Root.Inorder_Traversal(Root))
    print(Root.Preorder_Traversal(Root))
    print(Root.PostorderTraversal(Root))