# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

def reverseLinkedList(LnkLst,head):


    prev= None
    while head is not None :

        next = head.next  # Store head to next variable --> to 5 in first loop
        #print(next.data)
        head.next = prev  # point head in reverse direction to previous node.. In first loop ,it will be empty node --> 2 next node will be None in first loop
        #print(head.next.data)
        prev = head  # point NewHead to existing node --> will point to 2 in first loop
        #print(NewHead.data)
        head = next # point head to next node --> point head to 5 in first loop
        #print(head.data)

    return prev

def reverseLinkedList_recursion(LnkLst,head = None ,prev = None ):

    if head is None:
        return prev

    # save the next head to the variable and set current node's Next parameter to the previous one
    next = head.next
    head.next = prev
    # pass the next node as 'head' and current head as 'prev' parameter to function recursively
    return reverseLinkedList_recursion(LnkLst,next,head)

def main() :

    LnkLst = LL.LinkedList()
    LnkLst.InsertElementAtBegining(5)
    LnkLst.InsertElementAtBegining(2)
    LnkLst.InsertElementAtEnd(8)
    LnkLst.InsertElementAtEnd(9)
    LnkLst.InsertElementAtEnd(10)
    LnkLst.print_linked_list(LnkLst.head)

    # using while loop
    #new_head = reverseLinkedList(LnkLst,LnkLst.head)
    #LnkLst.print_linked_list(new_head)

    #using recursion
    #new_head_recur = reverseLinkedList_recursion(LnkLst,LnkLst.head)
    #LnkLst.print_linked_list(new_head_recur)

if __name__  == '__main__':
    main()