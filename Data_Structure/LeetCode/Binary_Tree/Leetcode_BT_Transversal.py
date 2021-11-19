Skip
to
content
Search or jump
to…
Pull
requests
Issues
Marketplace
Explore


@shyamsingh2706


shyamsingh2706
/
Python_HandsOn
Public
1
00
Code
Issues
Pull
requests
Actions
Projects
Wiki
Security
Insights
Settings
Python_HandsOn / Data_Structure / BInary_Search_Tree_Traversal.py /


@shyamsingh2706


shyamsingh2706
Update
BInary_Search_Tree_Traversal.py
Latest
commit
18
d8336
on
Oct
12
History
1
contributor
139
lines(109
sloc)  3.81
KB


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

    # Level order traversal
    def level_order_transversal(self, root):

        tree = []  ## Create a Queue for Tree to navigate tree in level order
        res = []  ## to print result

        if root == None:
            return 0

        tree.append(root)

        while len(tree) > 0:

            res.append(tree[0].data)
            node = tree.pop(0)

            if node.left:
                tree.append(node.left)

            if node.right:
                tree.append(node.right)

        return res

    def find_max_node(self):

        if self.RightChild is None:
            return self.data

        return self.RightChild.find_max_node()

    def find_min_node(self):

        if self.LeftChild is None:
            return self.data

        return self.LeftChild.find_min_node()

    def delete_node(self, data):

        if data > self.data:
            if self.RightChild:
                self.RightChild = self.RightChild.delete_node(data)
        elif data < self.data:
            if self.LeftChild:
                self.LeftChild = self.LeftChild.delete_node(data)
        else:
            if self.LeftChild is None and self.RightChild is None:
                return None
            elif self.LeftChild is None:
                return self.RightChild
            elif self.RightChild is None:
                return self.LeftChild

            # if Both Risk and left child nodes are present
            '''find min value from Right sub tree
            Assign to the node we are trying to delete
            then delete duplicate node
            assign modified sub tree to Right sub tree'''

            min_val = self.RightChild.find_min_node()
            self.data = min_val
            self.RightChild = self.RightChild.delete_node(min_val)

        return self


if __name__ == "__main__":
    Root = BST_NODE(3)
    Root.insert_node(4)
    Root.insert_node(1)
    Root.insert_node(2)
    Root.insert_node(9)
    Root.insert_node(6)
    Root.insert_node(7)
    print(Root.Inorder_Traversal(Root))
    print(Root.Preorder_Traversal(Root))
    print(Root.PostorderTraversal(Root))
    # print(Root.find_max_node())
    # print(Root.find_min_node())
    Root.delete_node(4)
    print(Root.Inorder_Traversal(Root))
    print(Root.Preorder_Traversal(Root))
    print(Root.PostorderTraversal(Root))
