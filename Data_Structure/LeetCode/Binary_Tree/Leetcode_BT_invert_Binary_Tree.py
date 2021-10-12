
class BT():

    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None
        self.result = 0

    def printLevelOrder(self,root):
        # Base Case
        if root is None:
            return

        # Create an empty queue
        # for level order traversal
        queue = []
        res = [] ## to capture level order transversal

        # Enqueue Root and initialize height
        queue.append(root)

        while (len(queue) > 0):

            # Print front of queue and
            # remove it from queue
            res.append(queue[0].data)
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

        return res

    def invert_BT(self,root):

        if root is None:
            return

        # Create an empty queue
        # for level order traversal
        queue = []

        # Enqueue Root and initialize height
        queue.append(root)

        while (len(queue) > 0):

            # Print front of queue and
            # remove it from queue

            node = queue.pop(0)
            node.left,node.right = node.right,node.left

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)



def main() :

    root = BT(4)
    root.left = BT(2)
    root.right = BT(7)
    root.left.left = BT(1)
    root.left.right = BT(3)
    root.right.left = BT(6)
    root.right.right = BT(9)

    print("tree level order transversal for BT is", root.printLevelOrder(root))
    root.invert_BT(root)
    print("tree level order transversal for Inverted BT is", root.printLevelOrder(root))

if __name__ == "__main__" :
    main()
