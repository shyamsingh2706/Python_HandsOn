# https://leetcode.com/problems/middle-of-the-linked-list/

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# create two pointers fast & slow.
# move slow by 1 step and fast by 2 step
# in the end , slow pointer will in middle of the linked list when fast will be in end of linked list

# time complxity : O(n/2) , space Complexity O(1)

import LC_LL_Singly_LL_Basics_Operations as LL

def middleNode(LnkLst,head) :

    slow = head
    fast = head

    if head is None:
        return

    while fast is not None and fast.next is not None :

        slow = slow.next
        fast = fast.next.next

    return slow



def main() :

    LnkLst = LL.LinkedList()
    LnkLst.InsertElementAtBegining(5)
    LnkLst.InsertElementAtBegining(2)
    LnkLst.InsertElementAtEnd(8)
    LnkLst.InsertElementAtEnd(9)
    LnkLst.InsertElementAtEnd(10)
    LnkLst.InsertElementAtEnd(12)
    LnkLst.print_linked_list(LnkLst.head)


    middle_element = middleNode(LnkLst,LnkLst.head)
    print("middle node of Linked list is " , LnkLst.print_linked_list(middle_element))

if __name__  == '__main__':
    main()