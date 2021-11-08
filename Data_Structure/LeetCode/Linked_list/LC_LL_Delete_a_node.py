# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Write a function to delete a node in a singly-linked list.
# You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.


import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next


def deleteNode(node):

    # in order to delete current node, we need to poin previous node to next to next node
    # but as we dont have previous node's information
    # we first copy next node value to current node
    # and then point current node to next of next node

    # i.e. skip next node of current node by copying its value on current node
    node.data = node.next.data
    node.next = node.next.next

    return


def main() :

    node1 =  node(1)
    node2 = node(2)
    node1.next = node2

    node3 = node(3)
    node2.next = node3

    node4 = node(4)
    node3.next = node4

    LnkLst = LL.LinkedList()
    LnkLst.print_linked_list(node1)


    deleteNode(node3)
    LnkLst.print_linked_list(node1)

if __name__  == '__main__':
    main()