# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

# Time Complxity O( n + m ) , Space complixity O( n + m )
def mergeTwoLists(head1,head2):

    # if one LL is empty and other is not , return the Non Empty linked list
    if head1 is None and head2 is not None:
        return head2
    if head1 is not None and head2 is None:
        return head1

    # create a new linked list to store the new merged sorted LL
    merged_LL =  LL.LinkedList()

    # iterate until both linked list are not empty
    while head1 is not None and head2 is not None :

        # if element in 2nd linked list element is greater than first LL element, add smaller element into LL
        # move to next element of 2nd linked list
        if head1.data > head2.data:
            merged_LL.InsertElementAtEnd(head2.data)
            head2 = head2.next

        # if element in first linked list is smaller then 2nd linked list element, add smaller element into LL
        # move to next element of 1st linked list
        else:
            merged_LL.InsertElementAtEnd(head1.data)
            head1 = head1.next

    # if first LL is not empty but 2nd LL is empty, append the rest of the element of first LL into new LL
    while head1 is not None and head2 is None:
        merged_LL.InsertElementAtEnd(head1.data)
        head1 = head1.next

    # if 2nd LL is not empty but 1st LL is empty, append the rest of the element of 2nd LL into new LL
    while head1 is None and head2 is not None:
        merged_LL.InsertElementAtEnd(head2.data)
        head2 = head2.next

    # return Head of new LL
    return merged_LL.head

# Time Complxity O( n + m ) , Space complixity O( 1 )
def mergeTwoLists_Optimized(head1,head2):

    # if one LL is empty and other is not , return the Non Empty linked list
    if head1 is None and head2 is not None:
        return head2
    if head1 is not None and head2 is None:
        return head1

    # if head2 is smaller , point head1 to smaller element
    if head1.data > head2.data :
        temp = head1
        head1 = head2
        head2 = temp

    # mark new head to head1 as it will point to smaller element
    new_head = head1

    # until head1 and head2 is not none
    while head1 is not None and head2 is not None :
        temp = None
        # Keep moving your head1 until element are smaller than head2 data
        while head1 is not None and head1.data <= head2.data :
                temp = head1
                head1 = head1.next

        # when you find an element thats greater then head.data
        # assign previous element next ( i.e. temp.next , previous smaller element ) to head2 and swap head1 & head 2
        temp.next = head2
        #swap
        temp = head1
        head1 = head2
        head2 = temp

    return new_head

def main() :

    LnkLst1 = LL.LinkedList()

    LnkLst1.InsertElementAtEnd(1)
    LnkLst1.InsertElementAtEnd(2)
    LnkLst1.InsertElementAtEnd(4)
    LnkLst1.print_linked_list(LnkLst1.head)

    LnkLst2 = LL.LinkedList()
    LnkLst2.InsertElementAtEnd(1)
    LnkLst2.InsertElementAtEnd(3)
    LnkLst2.InsertElementAtEnd(4)
    LnkLst2.InsertElementAtEnd(6)
    LnkLst2.InsertElementAtEnd(8)
    LnkLst2.print_linked_list(LnkLst2.head)

    new_head = mergeTwoLists(LnkLst1.head, LnkLst2.head)
    #new_head = mergeTwoLists_Optimized(LnkLst1.head, LnkLst2.head)

    LnkLst2.print_linked_list(new_head)

    new_head_op = mergeTwoLists_Optimized(LnkLst1.head, LnkLst2.head)
    # new_head = mergeTwoLists_Optimized(LnkLst1.head, LnkLst2.head)

    LnkLst2.print_linked_list(new_head_op)

if __name__  == '__main__':
    main()
