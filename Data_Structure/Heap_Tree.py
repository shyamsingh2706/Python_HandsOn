''' Program to create a MaxHeap and MinHeap tree
    1) Insert multiple element into Min & max Heap Tree
    2) delete an element from Min or Max Heap Tree
    3) Perform Heap Sort on Min or Max Heap tree
    4) Print the Heap tree after every addition of new element '''

class MaxHeap():

    def __init__(self):
        self.heap = []
        self.sorted_array = []

    # Function to find Parent element for a given child in heap Array
    def find_parent_index(self,self_index_val):

        if self_index_val in (1,2):
            return 0
        else:
            parent_index  = ((self_index_val-1) // 2)
            return parent_index

    # Function to Print the heap
    def __str__(self):
        Heap_elements = []
        for j in self.heap:
            Heap_elements.append(j)
        return f"{Heap_elements}"

    # Function to find Left child for a given parent element in heap Array
    def find_left_child_index(self,self_index_val):
        return ((2*self_index_val) + 1 )

    # Function to find Right child for a given parent element in heap Array
    def find_right_child_index(self,self_index_val):
        return ((2*self_index_val) + 2 )


    # Function to insert a element into maxHeap
    def insert_element(self,element):

        # Set the count to last element of the index
        index = len(self.heap)
        Loop_Count = 0

        if index == 0:
            # If heap is empty , insert the element
            self.heap.insert(index,element)
        else:
            # if Heap is not empty
            while True :
                # Find parent Index of newly inserted element
                parent_index = self.find_parent_index(index)

                # if newly created parent's element is greater than or equal to newly inserted element value
                # insert it at leaf most node only for first iteration
                if ( self.heap[parent_index] >= element ) :
                    if Loop_Count == 0 :
                        self.heap.insert(index,element)
                    break
                else:
                    # if newly created parent's element is less than or equal to newly inserted element value
                    # swap the parent and child in the heap tree
                    if Loop_Count == 0 :
                        # if very first iteration
                        # insert parent element as leaf node and swap newly created element at its parent's index
                        self.heap.insert(index,self.heap[parent_index])
                        self.heap[parent_index] = element
                    else:
                        # if not the first iteration
                        # swap the values of parent and child
                        self.heap[index] = self.heap[parent_index]
                        self.heap[parent_index] = element

                # Reset the index position to its parent position for next comparision
                index = parent_index
                Loop_Count = Loop_Count + 1

                # if reached Root Node , exit the loop and no more nodes are left for comparision
                if index == 0 :
                    break


    # delete a Element from a MaxHeap
    def Delete_Element(self):

        Index = len(self.heap)

        if (Index == 0 ):
            print ("Heap is empty")
        else:
            # replace Root node with leaf node
            # delete Leaf Node
            self.heap[0]=self.heap[-1]
            self.heap.pop(Index-1)

            #reset pointer to Root Node
            Index = 0

            # start iterating to Heap Tree
            while True:

                # find Right and Left child Index and set a flag if a given Child exists or not
                Right_child_index = self.find_right_child_index(Index)
                Left_child_index = self.find_left_child_index(Index)
                Right_child_exist ='N'
                Left_child_exist ='N'
                is_swapping_happen ='N'
                left_flag = 'N'
                right_flag = 'N'

                # logic to check if a given left and Right Node exists for a parent node
                if Right_child_index <= len(self.heap) - 1:
                    Right_child_exist = 'Y'
                if Left_child_index <= len(self.heap) - 1:
                    Left_child_exist = 'Y'

                # Logic to pick a given route for comparision of parent element with child element
                if Right_child_exist == 'Y' and Left_child_exist == 'Y':
                    if self.heap[Left_child_index] > self.heap[Right_child_index]:
                        left_flag = 'Y'
                    else:
                        right_flag = 'Y'
                elif Right_child_exist == 'Y' and Left_child_exist == 'N':
                    right_flag = 'Y'
                elif Right_child_exist == 'N' and Left_child_exist == 'Y':
                    left_flag = 'Y'

                # Break if No Left and Right child exists
                if ( right_flag == 'N' and left_flag == 'N'  ) :
                    break
                else:
                    # if Right child Exists
                    if right_flag == 'Y':
                        # if existing Node value is less that right child Node value
                        # swap the nodes
                        if (self.heap[Index] < self.heap[Right_child_index]):
                            Temp = self.heap[Right_child_index]
                            self.heap[Right_child_index] = self.heap[Index]
                            self.heap[Index] = Temp
                            is_swapping_happen ='Y'

                        # Reset Index only is Node swapping happened
                        # else continue to Left node comparision with existing index values
                        if (is_swapping_happen == 'Y') :
                            # reset index value to Right child's Node Index for further comparision
                            Index = Right_child_index
                            #Skip Left node comparision as one node is already swapped
                            continue

                    # if left Child Node exists
                    if left_flag == 'Y':
                        # if existing Node value is less that left child Node value
                        # swap the nodes
                         if (self.heap[Index] < self.heap[Left_child_index] ):
                            Temp = self.heap[Left_child_index]
                            self.heap[Left_child_index] = self.heap[Index]
                            self.heap[Index] = Temp
                            is_swapping_happen = 'Y'

                         if (is_swapping_happen == 'Y'):
                             # reset index value to Right child's Node Index for further comparision
                             Index = Left_child_index

                    # If Nodes exists but no swapping happened
                    # No need to iterate further
                    if is_swapping_happen == 'N':
                        break

    def HeapSort(self):

        while len(self.heap) > 0 :
            self.sorted_array.insert(0, self.heap[0])
            self.Delete_Element()


# Create a MinHeap Class by inheriting MaxHeap Class
class MinHeap(MaxHeap):

    # Override Insert Element function as per MinHeap Functionality
    # Function to insert a element into MinHeap
    def insert_element(self, element):

        # Set the count to last element of the index
        index = len(self.heap)
        Loop_Count = 0

        if index == 0:
            # If heap is empty , insert the element
            self.heap.insert(index, element)
        else:
            # if Heap is not empty
            while True:
                # Find parent Index of newly inserted element
                parent_index = self.find_parent_index(index)

                # if newly created parent's element is less than or equal to newly inserted element value
                # insert it at leaf most node only for first iteration
                if (self.heap[parent_index] <= element):
                    if Loop_Count == 0:
                        self.heap.insert(index, element)
                    break
                else:
                    # if newly created parent's element is greater than or equal to newly inserted element value
                    # swap the parent and child in the heap tree
                    if Loop_Count == 0:
                        # if very first iteration
                        # insert parent element as leaf node and swap newly created element at its parent's index
                        self.heap.insert(index, self.heap[parent_index])
                        self.heap[parent_index] = element
                    else:
                        # if not the first iteration
                        # swap the values of parent and child
                        self.heap[index] = self.heap[parent_index]
                        self.heap[parent_index] = element

                # Reset the index position to its parent position for next comparision
                index = parent_index
                Loop_Count = Loop_Count + 1

                # if reached Root Node , exit the loop and no more nodes are left for comparision
                if index == 0:
                    break

    # delete a Element from a MinHeap
    def Delete_Element(self):

        Index = len(self.heap)

        if (Index == 0):
            print("Heap is empty")
        else:
            # replace Root node with leaf node
            # delete Leaf Node
            self.heap[0] = self.heap[-1]
            self.heap.pop(Index - 1)

            # reset pointer to Root Node
            Index = 0

            # start iterating to Heap Tree
            while True:

                # find Right and Left child Index and set a flag if a given Child exists or not
                Right_child_index = self.find_right_child_index(Index)
                Left_child_index = self.find_left_child_index(Index)
                Right_child_exist = 'N'
                Left_child_exist = 'N'
                left_flag ='N'
                right_flag ='N'

                is_swapping_happen = 'N'

                # logic to check if a given left and Right Node exists for a parent node
                if Right_child_index <= len(self.heap) - 1:
                    Right_child_exist = 'Y'
                if Left_child_index <= len(self.heap) - 1:
                    Left_child_exist = 'Y'

                # Logic to pick a given route for comparision of parent element with child element
                if Right_child_exist == 'Y' and Left_child_exist =='Y' :
                    if self.heap[Left_child_index] < self.heap[Right_child_index]:
                        left_flag ='Y'
                    else:
                        right_flag ='Y'
                elif Right_child_exist == 'Y' and Left_child_exist =='N' :
                        right_flag = 'Y'
                elif Right_child_exist == 'N' and Left_child_exist =='Y':
                        left_flag ='Y'


                # Break if No Left and Right child exists
                if (left_flag == 'N' and right_flag == 'N'):
                    break
                else:
                    # if Right child Exists
                    if right_flag == 'Y':
                        # if existing Node value is Greater that right child Node value
                        # swap the nodes
                        if (self.heap[Index] > self.heap[Right_child_index]):
                            Temp = self.heap[Right_child_index]
                            self.heap[Right_child_index] = self.heap[Index]
                            self.heap[Index] = Temp
                            is_swapping_happen = 'Y'

                        # Reset Index only is Node swapping happened
                        # else continue to Left node comparision with existing index values
                        if (is_swapping_happen == 'Y'):
                            # reset index value to Right child's Node Index for further comparision
                            Index = Right_child_index
                            # Skip Left node comparision as one node is already swapped
                            continue

                    # if left Child Node exists
                    if left_flag == 'Y' :
                        # if existing Node value is Greater that left child Node value
                        # swap the nodes
                        if (self.heap[Index] > self.heap[Left_child_index]):
                            Temp = self.heap[Left_child_index]
                            self.heap[Left_child_index] = self.heap[Index]
                            self.heap[Index] = Temp
                            is_swapping_happen = 'Y'

                        if (is_swapping_happen == 'Y'):
                            # reset index value to Right child's Node Index for further comparision
                            Index = Left_child_index

                    # If Nodes exists but no swapping happened
                    # No need to iterate further
                    if is_swapping_happen == 'N':
                        break

def build_max_heap():

    maxheap = MaxHeap()
    Element = 10
    maxheap.insert_element(Element)
    print(f"max Heap after  adding {Element} is --> {maxheap}")
    Element = 34
    maxheap.insert_element(Element)
    print(f"max Heap after  adding {Element} is --> {maxheap}")
    Element = 7
    maxheap.insert_element(Element)
    print(f"max Heap after  adding {Element} is --> {maxheap}")
    Element = 13
    maxheap.insert_element(Element)
    print(f"max Heap after  adding {Element} is --> {maxheap}")
    Element = 23
    maxheap.insert_element(Element)
    print(f"max Heap after  adding {Element} is --> {maxheap}")
    Element = 50
    maxheap.insert_element(Element)
    print(f"max Heap after  adding {Element} is --> {maxheap}")
    Element = 45
    maxheap.insert_element(Element)

    # print(f"max Heap after  adding {Element} is --> {maxheap}")
    # print("Deleting the root element from MaxHeap")
    # maxheap.Delete_Element()
    # print(f"max Heap after  deleting root element is --> {maxheap}")
    # maxheap.Delete_Element()
    # print(f"max Heap after  deleting root element is --> {maxheap}")
    # maxheap.Delete_Element()
    # print(f"max Heap after  deleting root element is --> {maxheap}")
    # maxheap.Delete_Element()
    # print(f"max Heap after  deleting root element is --> {maxheap}")

    print("performing Heap Sorting ")
    maxheap.HeapSort();
    print(f"Min Heap after heap Sort is ( Ascending Order ) --> {maxheap.sorted_array}")

def build_min_heap():
    minheap = MinHeap()
    Element = 10
    minheap.insert_element(Element)
    print(f"Min Heap after  adding {Element} is --> {minheap}")
    Element = 34
    minheap.insert_element(Element)
    print(f"Min Heap after  adding {Element} is --> {minheap}")
    Element = 7
    minheap.insert_element(Element)
    print(f"Min Heap after  adding {Element} is --> {minheap}")
    Element = 13
    minheap.insert_element(Element)
    print(f"Min Heap after  adding {Element} is --> {minheap}")
    Element = 23
    minheap.insert_element(Element)
    print(f"Min Heap after  adding {Element} is --> {minheap}")
    Element = 2
    minheap.insert_element(Element)
    print(f"Min Heap after  adding {Element} is --> {minheap}")

    # print("Deleting the root element from MinHeap")
    # minheap.Delete_Element()
    # print(f"Min Heap after  deleting root MinHeap is --> {minheap}")
    # minheap.Delete_Element()
    # print(f"Min Heap after  deleting root element is --> {minheap}")
    # minheap.Delete_Element()
    # print(f"Min Heap after  deleting root element is --> {minheap}")
    # minheap.Delete_Element()
    # print(f"Min Heap after  deleting root element is --> {minheap}")

    print("performing Heap Sorting ")
    minheap.HeapSort();
    print(f"Min Heap after heap Sort is ( Descending Order ) --> {minheap.sorted_array}")

if __name__ == "__main__":

    build_max_heap()
    print("===========================")
    # build_min_heap()
