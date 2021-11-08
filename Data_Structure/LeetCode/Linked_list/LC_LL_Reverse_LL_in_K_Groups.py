# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

import LC_LL_Singly_LL_Basics_Operations as LL


class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

# Time complexity O(N) , space comlxity O(K) as we are using addtional stack to reverse the linked list
def reverseKGroup( head , k ):

    dummy = node()
    temp_ptr = dummy # create a temporary pointer
    itr = head
    stack = []

    while itr:
        counter = k
        while counter and itr:  # iterate the linked list for K number of time and nullify its next counter before adding into stack
            temp = itr.next
            itr.next = None
            stack.append(itr)
            counter -= 1
            itr = temp

        # length of stack is less that counter size, pop  like Queue i.e. FIFO
        if len(stack) < k:
            while stack:
                temp_ptr.next = stack.pop(0)
                temp_ptr = temp_ptr.next


        # length of stack is equal to size of counter size, pop  like stack i.e. in reverse order
        # use dummy node next to create next pointer to the element being popped from stack
        else:
            while stack:
                temp_ptr.next = stack.pop()
                temp_ptr = temp_ptr.next


    return dummy.next

# Time complexity O(N) , space comlxity O(1) as we are using addtional stack to reverse the linked list
def reverseKGroup_Optimized( head , k ):

    if head is None or k == 1 :
        return head

    dummy = node()
    dummy.next = head

    curr = dummy
    nex = dummy
    prev = dummy

    count = 0
    while curr.next is not None :
        curr = curr.next
        count += 1

    while count >= k :

        # Dummy & pre --> 1 ( curr ) --> 2 ( next ) --> 3

        curr = prev.next
        nex = curr.next

        for i in range(1,k):
            # now first couple elements are reversed
            curr.next = nex.next # break link between 1 & 2   #  1 --> 3
            nex.next = prev.next # break link between 2 & 3   #  2 --> 1
            prev.next = nex # now point prev to next # pre --> 2
            nex = curr.next # move next forward # next = 3 ( as per step 1 )

        prev = curr # point prev to curr i.e. element 1 ( last node in reversed list )
        count = count - k

    return dummy.next


def main() :

    LnkLst = LL.LinkedList()
    LnkLst.InsertElementAtEnd(1)
    LnkLst.InsertElementAtEnd(2)
    LnkLst.InsertElementAtEnd(3)
    LnkLst.InsertElementAtEnd(4)
    LnkLst.InsertElementAtEnd(5)
    LnkLst.InsertElementAtEnd(6)
    LnkLst.InsertElementAtEnd(7)
    LnkLst.print_linked_list(LnkLst.head)

    k = 3
    new_head = reverseKGroup_Optimized(LnkLst.head,k)
    LnkLst = LL.LinkedList()
    LnkLst.print_linked_list(new_head)

if __name__  == '__main__':
    main()