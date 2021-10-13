# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# https://www.geeksforgeeks.org/zigzag-tree-traversal/

from collections import deque

class BT():

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

    def level_order_transversal(self,root):


        tree = [] ## Create a Queue for Tree to navigate tree in level order
        res = [] ## to print result

        if root == None :
            return 0

        tree.append(root)

        while len(tree) > 0 :

            res.append(tree[0].data)
            node = tree.pop(0)

            if node.left :
                tree.append(node.left)

            if node.right :
                tree.append(node.right)

        return res

    def zigzag_level_order_transversal(self,root):

        # Create two stacks to store current
        # and next level
        Current_tree = []
        Next_tree = []

        res = []  ## to stroe & print result

        # if ltr is true push nodes from
        # left to right otherwise from
        # right to left
        itr = True

        if root == None:
            return

        Current_tree.append(root)

        while len(Current_tree) > 0:


            node = Current_tree.pop(-1)
            res.append(node.data)

            if itr :

                # if ltr is true push left
                # before right
                if node.left:
                    Next_tree.append(node.left)

                if node.right:
                    Next_tree.append(node.right)
            else:

                # else push right before left
                if node.right:
                    Next_tree.append(node.right)

                if node.left:
                    Next_tree.append(node.left)

            if len(Current_tree) == 0:
                # reverse ltr to push node in
                # opposite order
                itr = not itr
                # swapping of stacks
                Current_tree, Next_tree = Next_tree, Current_tree

        return res

    # Function to print the zigzag traversal
    def zigZagTraversal_2ndApproach(self,root):
        q = deque([])
        v = []
        q.append(root)
        v.append(root.data)

        # set initial level as 1, because root is
        # already been taken care of.
        l = 1

        while len(q) > 0:
            n = len(q)
            for i in range(n):
                # popping mechanism
                if (l % 2 == 0):
                    temp = q[-1]
                    q.pop()
                else:
                    temp = q[0]
                    q.popleft()

                # pushing mechanism
                if (l % 2 != 0):
                    if (temp.right):
                        q.append(temp.right)
                        v.append(temp.right.data)
                    if (temp.left):
                        q.append(temp.left)
                        v.append(temp.left.data)
                elif (l % 2 == 0):
                    if (temp.left):
                        q.appendleft(temp.left)
                        v.append(temp.left.data)
                    if (temp.right):
                        q.appendleft(temp.right)
                        v.append(temp.right.data)
            l += 1  # level plus one
        return v

    def pre_order_transversal(self,root):

        res = []

        if  root:

            res = self.pre_order_transversal(root.left)
            res.append(root.data)
            res = res + self.pre_order_transversal(root.right)

        return res

    def get_height(self,root):

        if root:

            Left_height = self.get_height(root.left)
            Right_height = self.get_height(root.right)
            if Left_height > Right_height :
                return Left_height + 1
            else:
                return Right_height + 1
        else:
            return 0

Q = deque()

# Helper function helps us in adding data
# to the tree in Level Order
def insert_node_level_order(data,root):

    newnode = BT(data)
    if Q:
        temp = Q[0]

    if root == None:
        root= newnode

    # The left child of the current Node is
    # used if it is available.
    elif temp.left == None:
        temp.left= newnode

    # The right child of the current Node is used
    # if it is available. Since the left child of this
    # node has already been used, the Node is popped
    # from the queue after using its right child.
    elif temp.right == None:
        temp.right = newnode
        atemp = Q.popleft()

    Q.append(newnode)
    return root

# Function which calls add which is responsible
# for adding elements one by one
def createTree(a, root):
    for i in range(len(a)):
        root = insert_node_level_order(a[i], root)
    return root

def main() :

    arr = [4,2,7,1,3,6,9]
    root = None
    root=createTree(arr,root)

    print("tree level order transversal for BT is", root.level_order_transversal(root))
    print("Zigzag tree level order transversal for BT is", root.zigzag_level_order_transversal(root))
    print("Zigzag tree level order transversal for BT with 2nd Approach is", root.zigZagTraversal_2ndApproach(root))

if __name__ == "__main__" :
    main()
