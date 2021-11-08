# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

# Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]

# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5].
# There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB) :

        self.itr1 = headA
        self.itr2 = headB
        self.swap_head1 = 'N'
        self.swap_head2 = 'N'

        while self.itr1 is not None or self.itr2 is not None:

            # if list 1 & list 2 has different length , then we will stop loop after 2nd iteration
            # for first iteration , we just reset pointer to head of another linked list to mitigate the difference of length
            if self.itr1 is None and self.swap_head1 == 'N':
                self.itr1 = headB
                self.swap_head1 = 'Y'

            if self.itr2 is None and self.swap_head2 == 'N':
                self.itr2 = headA
                self.swap_head2 = 'Y'

            # if a node is same in both linked list, return its value
            if self.itr1 == self.itr2:
                return self.itr1.data

            self.itr1 = self.itr1.next
            self.itr2 = self.itr2.next

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
    LnkLst = LL.LinkedList()
    LnkLst.print_linked_list(node1)

    node01 = node(5)
    node02 = node(6)
    node01.next = node02
    node03 = node(1)
    node02.next = node03
    node04 =  node3
    node03.next = node04
    node05 = node(4)
    node04.next = node05
    node06 = node(5)
    node05.next = node06
    LnkLst.print_linked_list(node01)

    sol = Solution()
    intersect_num = sol.getIntersectionNode(node1,node01)
    print("Intersection node is : " , intersect_num)

if __name__  == '__main__':
    main()
