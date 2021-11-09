# https://leetcode.com/problems/rotate-list/
# Given the head of a linked list, rotate the list to the right by k places.


import LC_LL_Singly_LL_Basics_Operations as LL

class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next


def rotateRight(head,k):

    # edge cases
    if head is None or head.next is None or k == 0 :
        return head

    # take count of existing linked list
    cur = head
    len = 1
    while cur.next:
        cur = cur.next
        len += 1

    # point last node to head
    cur.next = head

    # take the number of time we need to rotate the linked list if k is more that linked list length
    # go til that node i.e. total length - rotation count
    rotation_count = k % len
    k = len - rotation_count

    # move slow pointer to number of time rotation is neded
    while k != 0 :

        cur = cur.next
        k = k - 1

    # repoint elements
    head = cur.next # point slow next element to current head
    cur.next = None # nullify the slow next element to None i.e. as end of the list

    return head # return new head


def main() :

    LnkLst = LL.LinkedList()
    LnkLst.InsertElementAtEnd(1)
    LnkLst.InsertElementAtEnd(2)
    LnkLst.InsertElementAtEnd(3)
    LnkLst.InsertElementAtEnd(4)
    LnkLst.InsertElementAtEnd(5)
    LnkLst.print_linked_list(LnkLst.head)

    k = 3
    new_head_recur = rotateRight(LnkLst.head,k)
    LnkLst.print_linked_list(new_head_recur)

if __name__  == '__main__':
    main()