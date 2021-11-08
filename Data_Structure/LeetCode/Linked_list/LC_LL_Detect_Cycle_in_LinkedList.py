# https://leetcode.com/problems/linked-list-cycle/

#  Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.


import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

def hasCycle(head):

    fast = head
    slow = head

    if head is None or head.next is None :
        return False

    # using flood cycle detection
    # move slow pointer by 1 and fast pointer by 3
    # if there is a cycle, it will collide at some point else it wont
    while slow and fast :

        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

        if fast == slow:
            return True

    return False

def main() :

    node1 = node(4)
    node2 = node(1)
    node1.next = node2
    node3 = node(8)
    node2.next = node3
    node4 = node(4)
    node3.next = node4
    node5 = node(5)
    node4.next = node5

    node5.next = node3
    #LnkLst = LL.LinkedList()
    #LnkLst.print_linked_list(node1)

    res = hasCycle(node1)
    print("given linked list has cycle : " , res)

if __name__  == '__main__':
    main()