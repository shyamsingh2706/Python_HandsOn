# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

import LC_LL_Singly_LL_Basics_Operations as LL


def addTwoNumbers(head1,head2):

    Carry = 0

    itr1 = head1
    itr2 = head2
    SumLL = LL.LinkedList()

    while itr1 is not None or itr2 is not None or Carry:

        Sum = 0
        if itr1 is not None :
            Sum = Sum + itr1.data
            itr1 = itr1.next

        if itr2 is not None:
            Sum = Sum + itr2.data
            itr2 = itr2.next

        Sum = Sum + Carry
        Carry = Sum // 10
        node = Sum % 10
        SumLL.InsertElementAtEnd(node)

    SumLL.print_linked_list(SumLL.head)

    return

def main() :

    LnkLst1 = LL.LinkedList()

    LnkLst1.InsertElementAtEnd(2)
    LnkLst1.InsertElementAtEnd(4)
    LnkLst1.InsertElementAtEnd(3)
    LnkLst1.print_linked_list(LnkLst1.head)

    LnkLst2 = LL.LinkedList()
    LnkLst2.InsertElementAtEnd(5)
    LnkLst2.InsertElementAtEnd(6)
    LnkLst2.InsertElementAtEnd(9)
    LnkLst2.InsertElementAtEnd(8)
    LnkLst2.print_linked_list(LnkLst2.head)

    addTwoNumbers(LnkLst1.head,LnkLst2.head)

if __name__  == '__main__':
    main()