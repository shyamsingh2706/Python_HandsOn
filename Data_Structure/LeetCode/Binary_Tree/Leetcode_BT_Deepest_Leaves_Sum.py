# https://leetcode.com/problems/deepest-leaves-sum/
# https://www.geeksforgeeks.org/sum-leaf-nodes-binary-tree/


from collections import deque,defaultdict

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

    def deepest_leaves_Sum(self,root):

        dir = {}
        lvl = 0
        temp = []
        current_tree =[]
        next_tree = []
        itr = True

        if root == None :
            return 0

        current_tree.append(root)
        dir[lvl] = root.data

        while len(current_tree) > 0 :

            node = current_tree.pop(0)
            if itr :

                if node.left :
                    next_tree.append(node.left)
                    temp.append(node.left.data)
                if node.right :
                    next_tree.append(node.right)
                    temp.append(node.right.data)
            else:

                if node.left :
                    next_tree.append(node.left)
                    temp.append(node.left.data)
                if node.right :
                    next_tree.append(node.right)
                    temp.append(node.right.data)

            if len(current_tree) == 0:

                itr = not itr
                current_tree,next_tree = next_tree,current_tree
                lvl += 1
                if len(temp) > 0 :
                    dir[lvl] = temp
                    temp= []

        res = 0
        for j in dir[max(dir.keys())] :
            if j :
                res = res + j

        return res

    def deepestLeavesSum(self, root):
        queue = [[root, 0]]
        res = defaultdict(list)

        while (queue):
            node, val = queue.pop(0)
            if node.left:
                queue.append([node.left, val + 1])
                res[val + 1].append(node.left.data)
            if node.right:
                queue.append([node.right, val + 1])
                res[val + 1].append(node.right.data)

        maxKey = 0
        for key in res:
            maxKey = max(maxKey, key)

        sum = 0
        for j in res[maxKey]:
            if j:
                sum = sum + j

        return sum

    def pre_order_transversal(self,root):

        res = []

        if  root:

            res = self.pre_order_transversal(root.left)
            res.append(root.data)
            res = res + self.pre_order_transversal(root.right)

        return res


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

    arr = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    root = None
    root=createTree(arr,root)

    print("tree level order transversal for BT is", root.level_order_transversal(root))
    print("Deepest_leaves sum for BT is", root.deepestLeavesSum(root))

if __name__ == "__main__" :
    main()