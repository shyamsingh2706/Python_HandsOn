''' Python Program to replicate Linked List features'''

# Create a node class to create a Note and store the reference of next Node object
class node():

    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next


# Class to create a linked List Object
class lnkList():

    ''' function to Initialize the linked list object reference as None '''
    def __init__(self):
         self.head = None

    '''  Function to Insert a element in Begining of the linked list  '''
    def insert_element_at_begining(self,element):
        # Create a Node and assign previous Node's reference to it in order to iterate
        Node = node(element,self.head)
        # reset newly created Node's object reference to self.head for next Node creation
        self.head = Node

    '''  Function to Insert a element in End of the linked list  '''
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

    ''' Function to print a linked list '''
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

    ''' Function to Insert multiple element at a time into Linked list '''
    def insert_values(self,elements):
        for j in elements:
            self.insert_element_at_end(j)

    ''' Function to get Length of Linked List '''
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

            #print(f"linked LIst length is {count}")
            return int(count)


    ''' Function to Remove an Item from Linked list at a given Index from start assuming first index as 0 '''
    def remove_at(self,index):

        if self.head is None:
            print ("linked LIst is Empty")
        elif (index < 0 or index > self.get_length()):
            print("Invalid_input")
        else:

            itr_prev = self.head
            itr = self.head
            count = 0
            while itr:
                if (index > 0 and index == count):
                    itr_prev.next = itr.next
                    break
                elif (index == 0 ):
                    self.head = itr.next
                    break
                itr_prev = itr
                itr = itr.next
                count = count + 1


    ''' Function to Insert an Item into a Linked list at a given Index from start assuming first index as 0 '''
    def insert_at(self,index,element):

        if (index == 0 ) :
            self.insert_element_at_begining(element)
        else:

            itr_prev = self.head
            itr = self.head
            count = 0
            while itr:

                if (index > 0 and index == count ):

                    new_node = node(element)
                    new_node.next = itr_prev.next
                    itr_prev.next = new_node
                    break

                itr_prev = itr
                itr = itr.next
                count = count + 1


    ''' Function to Insert an Item into a Linked list after a given value ( first instance from start) '''
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    def insert_after_value(self,data_after, data_to_insert):

        itr = self.head
        itr_prev = self.head

        while itr:
            if (itr.data == data_after):

                new_node = node(data_to_insert)
                itr_prev = itr
                itr = itr.next
                new_node.next = itr_prev.next
                itr_prev.next = new_node
                break

            itr_prev = itr
            itr = itr.next

    ''' Function to Remove an Item based on a value ( first instance of the value from start) '''
    # Remove first node that contains data
    def remove_by_value(self,element):

        itr = self.head
        itr_prev = self.head
        count = 0
        while itr:

            if (itr.data == element and count == 0 ):
                self.head = itr.next
                break
            elif (itr.data == element and count > 0 ):
                itr_prev.next = itr.next
                break

            itr_prev = itr
            itr = itr.next
            count = count + 1

if __name__ == "__main__":

    ll = lnkList()
    len = ll.get_length()
    print(f"Linked list length is {len}")
    print("Adding elements one by one in linked list and printing the same")
    ll.insert_element_at_begining(23)
    ll.insert_element_at_begining(1)
    ll.insert_element_at_end(2)
    ll.insert_element_at_begining(10)
    ll.printll()
    print("Adding Multiple elements in linked list and printing the same")
    ll.insert_values([100,200,300])
    ll.printll()
    len = ll.get_length()
    print ( f"Linked list length is {len}")
    print("Removing element based on Index and printing Linked list afterwards")
    ll.remove_at(2)
    ll.printll()
    ll.remove_at(0)
    ll.printll()
    ll.remove_at(10)
    ll.printll()
    print("Adding element based on Index and printing Linked list afterwards")
    ll.insert_at(0,123)
    ll.printll()
    ll.insert_at(2, 250)
    ll.printll()
    print("Adding element based on Value and printing Linked list afterwards")
    ll.insert_after_value(100,333)
    ll.printll()
    print("Removing element based on Value and printing Linked list afterwards")
    ll.remove_by_value(250)
    ll.printll()
    ll.remove_by_value(123)
    ll.printll()