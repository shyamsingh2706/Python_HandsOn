# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        new_head = None

        for l in lists:

            if new_head is None:

                new_head = l

            else:

                new_head = self.mergeTwoList(l, new_head)

        return new_head

    def mergeTwoList(self, head1, head2):

        # if one LL is empty and other is not , return the Non Empty linked list
        if head1 is None and head2 is not None:
            return head2
        if head1 is not None and head2 is None:
            return head1

        # if head2 is smaller , point head1 to smaller element
        if head1.val > head2.val:
            temp = head1
            head1 = head2
            head2 = temp

        # mark new head to head1 as it will point to smaller element
        new_head = head1

        # until head1 and head2 is not none
        while head1 is not None and head2 is not None:
            temp = None
            # Keep moving your head1 until element are smaller than head2 data
            while head1 is not None and head1.val <= head2.val:
                temp = head1
                head1 = head1.next

            # when you find an element thats greater then head.data
            # assign previous element next ( i.e. temp.next , previous smaller element ) to head2 and swap head1 & head 2
            temp.next = head2
            # swap
            temp = head1
            head1 = head2
            head2 = temp

        return new_head