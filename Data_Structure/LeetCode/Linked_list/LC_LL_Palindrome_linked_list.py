# https://leetcode.com/problems/palindrome-linked-list/
# Given the head of a singly linked list, return true if it is a palindrome.

# Input: head = [1,2,2,1]
# Output: true

import LC_LL_Singly_LL_Basics_Operations as LL

def reverse_LL(head):

    prev =  None
    next = None

    while head is not None:

        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

def isPalindrome(head):

    if head is None or head.next is None:
            return True

    # find middle Node ( if even , first element of middle node ) as if palindrome , left and right half should be equal
    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        fast = fast.next
        if fast.next is not None:
            slow = slow.next
            fast = fast.next

    mid_lement = slow

    # reverse linked list post middle element
    # post reverse , first and 2nd half should be exactly equal
    reverse_node = reverse_LL(mid_lement.next)
    mid_lement.next = reverse_node

    LnkLst = LL.LinkedList()
    LnkLst.print_linked_list(head)

    # now compare first and 2nd half of modified linked list
    # move pointer to next element of middle element and start comparing it with first node i.e. head

    slow = mid_lement.next
    while slow is not None:
        if slow.data != head.data:
            return False

        head = head.next
        slow = slow.next

    return True

def main() :

    LnkLst = LL.LinkedList()
    LnkLst.InsertElementAtEnd(1)
    LnkLst.InsertElementAtEnd(2)
    LnkLst.InsertElementAtEnd(3)
    LnkLst.InsertElementAtEnd(2)
    LnkLst.InsertElementAtEnd(1)
    LnkLst.print_linked_list(LnkLst.head)
    res = isPalindrome(LnkLst.head)
    print("given linked list is Palindrome : ", res)

if __name__  == '__main__':
    main()