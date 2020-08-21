''' Python Program to replicate Linked List features'''

# Create a node class to create a Note and store the reference of next Node object
class node():

    def __init__(self,data=None, next = None , prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# Class to create a doubly linked List Object
class DoublnkList():

    ''' function to Initialize the linked list object reference as None '''
    def __init__(self):
         self.head = None

    '''  Function to Insert a element in Begining of the doubly linked list  '''
    def insert_element_at_begining(self,element):
        # Create a Node and assign previous Node's reference to it in order to iterate , next node reference as None
        Node = node(element,self.head,None)
        # reset newly created Node's object reference to self.head for next Node creation
        itr = self.head
        self.head = Node

        # If double linked List is not Empty , assign previous element's previous attribute to newly created node
        if itr :
            itr.prev = Node

    '''  Function to Insert a element in End of the doubly linked list  '''
    def insert_element_at_end(self,element):

        ''' if doubly linked list is empty
        create a node --> set next & prev element's reference as None
        --> assign self.head to newly created node's reference '''

        if self.head is None:
            Node = node(element,None,None)
            self.head = Node
            return

        # if list is not empty and self.head as reference to previous create node

        # pull current Node's reference
        itr = self.head

        # Find next object reference and iterate until reach the last element
        while itr.next:
            itr = itr.next

        # once reached last element , create a node with prev value as existing node and next object as None
        # assign its reference value to previous element's next attribute
        Node = node(element,None,itr)
        itr.next = Node

    ''' Function to print a doubly linked list from start to end '''
    def ForwardPrintAll(self):

        # if no object is present , linked list if empty
        if self.head is None :
            print("linked list is empty")
            return

        # if linked list is not empty , pick the latest object and interate over to pick next element and print it
        itr = self.head
        llstr = ''

        while itr :
            llstr += str(itr.data) +  '---->'
            itr = itr.next

        print(llstr)

    ''' Function to print a doubly linked list from End to Start '''
    def BackwardPrintAll(self):

        # if no object is present , linked list if empty
        if self.head is None:
            print("linked list is empty")
            return

        # if linked list is not empty , pick the latest object and Iterate over until last element
        itr = self.head
        while itr.next:
            itr = itr.next

        llstr = ''

        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.prev

        print(llstr)

    ''' Function to Insert multiple element at a time into doubly Linked list '''

    def insert_values(self, elements):
        for j in elements:
            self.insert_element_at_end(j)

    ''' Function to get Length of doubly Linked List '''

    def get_length(self):

        count = 0
        # if linked list is empty
        if self.head is None:
            # print(f"linked LIst length is {count}")
            return int(count)

        else:

            # if linked list is not empty , pick the latest object and iterate over to elements check the count
            itr = self.head
            while itr:
                count = count + 1
                itr = itr.next

            # print(f"linked LIst length is {count}")
            return int(count)

    ''' Function to Remove an Item from doubly Linked list at a given Index from start assuming first index as 0 '''

    def remove_at(self, index):

        if self.head is None:
            print("linked LIst is Empty")
        elif (index < 0 or index > self.get_length()-1):
            print("Invalid_input")
        elif (index > 0 or index <= self.get_length()-1):

            itr_prev = self.head
            itr = self.head
            count = 0
            while itr:
                if (index > 0 and index == count and index < self.get_length()-1):
                    next_ele = itr.next
                    itr_prev.next = itr.next
                    next_ele.prev = itr_prev
                    break
                if (index > 0 and index == count and index == self.get_length()-1):
                    prev_ele = itr.prev
                    prev_ele.next = None
                    break
                elif (index == 0):
                    next_ele = itr.next
                    self.head = itr.next
                    next_ele.prev = None
                    break
                itr_prev = itr
                itr = itr.next
                count = count + 1

    ''' Function to Insert an Item into a doubly Linked list at a given Index from start assuming first index as 0 '''
    def insert_at(self, index, element):

        if (index < 0 or index > self.get_length() - 1):
            print("Invalid_input")
        elif (index == 0):
            self.insert_element_at_begining(element)
        else:

            itr_prev = self.head
            itr = self.head
            count = 0
            while itr:

                if (index > 0 and index == count):
                    new_node = node(element)

                    new_node.next = itr
                    new_node.prev = itr_prev
                    itr_prev.next = new_node
                    itr.prev = new_node

                    break

                itr_prev = itr
                itr = itr.next
                count = count + 1


if __name__ == "__main__":

    ll = DoublnkList()
    print("Adding elements one by one in linked list and printing the same")
    ll.insert_element_at_begining(23)
    ll.insert_element_at_end(2)
    ll.insert_element_at_end(5)
    ll.insert_element_at_begining(10)
    ll.insert_element_at_end(7)
    ll.insert_element_at_begining(11)
    print("printing Doubly Linked list from start to end ")
    ll.ForwardPrintAll()
    print("printing Doubly Linked list from End to end ")
    ll.BackwardPrintAll()
    len = ll.get_length()
    print(f"Linked list length is {len}")
    print("Adding Multiple elements in linked list and printing the same")
    ll.insert_values([100, 200, 300])
    print("printing Doubly Linked list from start to end ")
    ll.ForwardPrintAll()
    print("printing Doubly Linked list from End to end ")
    ll.BackwardPrintAll()
    len = ll.get_length()
    print(f"Linked list length is {len}")
    print("Removing random element based on Index and printing Linked list afterwards")
    ll.remove_at(2)
    print("printing Doubly Linked list from start to end ")
    ll.ForwardPrintAll()
    print("printing Doubly Linked list from End to end ")
    ll.BackwardPrintAll()
    len = ll.get_length()
    print(f"Linked list length is {len}")
    print("Removing first element based on Index and printing Linked list afterwards")
    ll.remove_at(0)
    print("printing Doubly Linked list from start to end ")
    ll.ForwardPrintAll()
    print("printing Doubly Linked list from End to end ")
    ll.BackwardPrintAll()
    len = ll.get_length()
    print(f"Linked list length is {len}")
    print("Removing last element based on Index and printing Linked list afterwards")
    ll.remove_at(6)
    print("printing Doubly Linked list from start to end ")
    ll.ForwardPrintAll()
    print("printing Doubly Linked list from End to end ")
    ll.BackwardPrintAll()
    len = ll.get_length()
    print(f"Linked list length is {len}")
    print("Adding element based on Index and printing Linked list afterwards")
    ll.insert_at(5,456)
    print("printing Doubly Linked list from start to end ")
    ll.ForwardPrintAll()
    print("printing Doubly Linked list from End to end ")
    ll.BackwardPrintAll()
    len = ll.get_length()
    print(f"Linked list length is {len}")
    print("Adding element based on Index and printing Linked list afterwards")