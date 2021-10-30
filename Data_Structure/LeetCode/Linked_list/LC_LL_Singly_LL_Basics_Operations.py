''' Python Program to replicate Linked List features '''

# Create a node class to create a Note and store the reference of next Node object
class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next


class LinkedList() :

    def __init__(self,head = None):
        self.head = head

    def print_linked_list(self,head):

        if head is None:
            print("Empty Linked List")
            return

        itr = head
        LL = ''
        while itr:

            LL += str(itr.data) + ' --> '
            itr = itr.next

        LL += 'NULL'
        print(LL)


    def InsertElementAtBegining(self, element):

        NewNode = node(element)
        if self.head is None:
            self.head = NewNode
            return

        itr = self.head
        self.head = NewNode
        NewNode.next = itr

        return

    def InsertElementAtEnd(self,element):

        NewNode = node(element)
        if self.head is None:
            self.head = NewNode
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = NewNode
        return

    def RemoveElementAtEnd(self):

        if self.head is None:
            return

        itr = self.head
        while itr.next:
            itr_prev = itr
            itr = itr.next

        itr_prev.next = None
        return

    def RemoveElementAtBegining(self):

        if self.head is None:
            return

        itr = self.head
        self.head = itr.next

        return

def BuildLinkedList():

    LnkLst = LinkedList()
    LnkLst.InsertElementAtBegining(5)
    LnkLst.InsertElementAtBegining(2)
    LnkLst.InsertElementAtEnd(8)
    LnkLst.InsertElementAtEnd(9)
    LnkLst.InsertElementAtEnd(10)
    LnkLst.print_linked_list(LnkLst.head)
    LnkLst.RemoveElementAtEnd()
    LnkLst.print_linked_list(LnkLst.head)
    LnkLst.RemoveElementAtBegining()
    LnkLst.print_linked_list(LnkLst.head)

def main():

    BuildLinkedList()


if __name__  == '__main__':
    main()