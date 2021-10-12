
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

        # Enqueue Root and initialize height
        queue.append(root)

        while (len(queue) > 0):

            # Print front of queue and
            # remove it from queue
            print(queue[0].data)
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)


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
            print(queue[0].data)
            node = queue.pop(0)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)




def main() :

    root = BT(4)
    root.left = BT(2)
    root.right = BT(7)
    root.left.left = BT(1)
    root.left.right = BT(3)
    root.right.left = BT(6)
    root.right.right = BT(9)

    print("tree level order transversal for Inverted BT is", root.invert_BT(root))


if __name__ == "__main__" :
    main()