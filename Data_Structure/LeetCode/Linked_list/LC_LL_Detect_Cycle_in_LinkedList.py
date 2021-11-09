# https://leetcode.com/problems/linked-list-cycle/
# https://leetcode.com/problems/linked-list-cycle-ii/


#  Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.


import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

# https://leetcode.com/problems/linked-list-cycle/
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

# https://leetcode.com/problems/linked-list-cycle-ii/
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
def detectCycle(head):

    fast = head
    slow = head
    entry = head
    has_cycle = False

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
            has_cycle = True
            break

    # if it has cycle, start moving slow and entry pointer toghether, where ever they collide
    # will be entry point of cycle
    if has_cycle :

        while slow and entry :

            if slow == entry :
                return slow.data

            slow = slow.next
            entry = entry.next
    else:

        return None

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

    cycle_node = detectCycle(node1)
    print("given linked list has cycle and strting node of cycle is : ", cycle_node)

if __name__  == '__main__':
    main()
