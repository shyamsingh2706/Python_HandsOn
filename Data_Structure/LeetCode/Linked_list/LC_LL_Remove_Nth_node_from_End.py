# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

#Given the head of a linked list, remove the nth node from the end of the list and return its head.


import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

class solution():
    def removeNthFromEnd(self,LnkLst,head,n):

        start = node()
        start.next = head
        fast = start
        slow = start
        cntr = 1

        # move start counter until N times LL iteration is done
        while cntr <= n:
            cntr += 1
            fast = fast.next

        # if end of the list, no need to navigate further
        # that means , head node need to be deleled
        # if no means, some node in middle of the linked list need to be delete and further navigation is needed to find that element

        if fast.next is not None :
            AlreadyEndofTheList = 'N'
        else:
            AlreadyEndofTheList ='Y'

        if AlreadyEndofTheList == 'N':
            # once done, move start and end pointer toghether until end of the list
            while fast.next is not None :

                fast = fast.next
                slow = slow.next

            # now end pointer's next will be the node we want to delete
            # so to delete it, point end.next to its next to next node
            slow.next = slow.next.next

        else:
            # repoint head node to next node of origin node
            head = slow.next.next

        return head

def main() :

    LnkLst = LL.LinkedList()
    LnkLst.InsertElementAtBegining(5)
    LnkLst.InsertElementAtBegining(2)
    LnkLst.InsertElementAtEnd(8)
    LnkLst.InsertElementAtEnd(9)
    LnkLst.InsertElementAtEnd(10)
    LnkLst.InsertElementAtBegining(1)
    LnkLst.print_linked_list(LnkLst.head)

    S = solution()
    head = S.removeNthFromEnd(LnkLst,LnkLst.head,1)
    LnkLst.print_linked_list(head)

if __name__  == '__main__':
    main()