
# Create a node class to create a Note and store the reference of next Node object
class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next


# Class to create a linked List Object
class lnkList():

    # Initialize the linked list object reference as None
    def __init__(self):
         self.head = None

    # Definition to Insert a element in Begining of the linked list

    def insert_element_at_begining(self,element):
        # Create a Node and assign previous Node's reference to it in order to iterate
        Node = node(element,self.head)
        # reset newly created Node's object reference to self.head for next Node creation
        self.head = Node

    def insert_element_at_end(self,element):

        ''' if linked list is empty
        create a node --> set next element's reference as None --> assign self.head to newly created node's reference '''

        if self.head is None:
            Node = node(element,None)
            self.head = Node
            return

        # if list is not empty and self.head as reference to previous create node

        # pull current Node's reference
        itr = self.head

        # Find next object reference and iterate until reach the last element
        while itr.next:
            itr = itr.next

        # once reached last element , create a node and assing its reference value to previous element's next attribute
        Node = node(element,None)
        itr.next = Node

    # Function to print a linked list
    def printll(self):

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


    def insert_values(self):
        pass

    def get_length(self):
        pass

    def remove_at(self):
        pass

    def insert_at(self):
        pass

    def insert_after_value(self):
        pass

    def remove_by_value(self):
        pass

if __name__ == "__main__":

    ll = lnkList()
    ll.insert_element_at_begining(23)
    ll.insert_element_at_begining(1)
    ll.insert_element_at_end(2)
    ll.insert_element_at_begining(10)
    ll.printll()