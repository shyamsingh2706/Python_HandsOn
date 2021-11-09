
# https://leetcode.com/problems/lru-cache/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

    # LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    # int get(int key) Return the value of the key if the key exists, otherwise return -1.
    # void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    # The functions get and put must each run in O(1) average time complexity.

# doubly linked list node class
class node():

    def __init__(self,key=None,data=None, next = None,prev = None):
        self.key  = key
        self.data = data
        self.next = next
        self.prev = prev


class LRUCache :

    def __init__(self,capacity ):

        # creaet head & tail of LRU
        self.head = node()
        self.tail = node()

        # point both to each other as doubly linkedlist
        self.head.next = self.tail
        self.tail.prev = self.head

        # create dictionary i.e. hash map to store node and its associated address as a Cache
        self.dict = {}
        # initlialize cache capacity
        self.CacheSize = capacity

    # add element in LRU cache
    def insert_element(self,node):

        # insert it next to head i.e. as first element
        temp = self.head.next   # store head next to temp
        node.next = temp   # point newly added node's next to current head's next
        node.prev = self.head  # point newly added node's prev to head
        self.head.next = node # point current head's next node to newly created node
        temp.prev = node # point current head's next node's previous node to newly created node

    # delete element in LRU cache
    def delete_element(self,node):

        # capture prev & next node of deleted node
        del_prev = node.prev
        del_next = node.next
        # point prev node's next node to deleted node's next node
        del_prev.next = del_next
        # point next node's prev node to deleted node's previous node
        del_next.prev = del_prev


    def put(self,key,value):

        # if key is part of dict already
        if key in self.dict.keys():
            # find out its address
            node_addr = self.dict[key]
            # update its value in linked list using above fetched adress
            node_addr.data = value
            # delete the node from LRU cache
            self.delete_element(node_addr)
            # add it back next to head as its accessed recently
            self.insert_element(node_addr)
        else:
            # if key is not part of dict already
            # create a new node
            new_node = node(key,value)
            # if cache limit is not full
            if len(self.dict) < self.CacheSize:
                # update dictionary
                self.dict[key] = new_node
                # add element next to head
                self.insert_element(new_node)

            else:
                # if cache limit is  full
                if len(self.dict) >= self.CacheSize:
                    # delete LRU node ( previous of tail ) from dict
                    # update dictionary for new node
                    del self.dict[self.tail.prev.key]
                    self.dict[key] = new_node
                    # delele element from LRU
                    self.delete_element(self.tail.prev)
                    # delele newly added element into LRU
                    self.insert_element(new_node)

    # get a key from LRU
    def get(self, key):

        # present in dict
        if key in self.dict.keys():
            # get node's address
            node_addr = self.dict[key]
            # delete the node from LRU cache
            self.delete_element(node_addr)
            # add the node into LRU cache next to head
            self.insert_element(node_addr)
            # return its value using node's address
            return node_addr.data
        else:
             return -1

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


def main():

    lru = LRUCache(2)

    lru.put(1,0)
    lru.print_linked_list(lru.head)
    lru.put(2,2)
    lru.print_linked_list(lru.head)
    OutPut = lru.get(1)
    print("Element value is ",OutPut )
    lru.print_linked_list(lru.head)
    lru.put(3,3)
    lru.print_linked_list(lru.head)
    OutPut = lru.get(2)
    print("Element value is ", OutPut)
    lru.print_linked_list(lru.head)
    lru.put(4, 4)
    lru.print_linked_list(lru.head)
    OutPut = lru.get(1)
    print("Element value is ", OutPut)
    lru.print_linked_list(lru.head)
    OutPut = lru.get(3)
    print("Element value is ", OutPut)
    lru.print_linked_list(lru.head)
    OutPut = lru.get(4)
    print("Element value is ", OutPut)
    lru.print_linked_list(lru.head)
if __name__ == '__main__':
    main()