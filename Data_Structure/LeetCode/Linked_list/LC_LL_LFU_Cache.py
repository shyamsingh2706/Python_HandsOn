# https://leetcode.com/problems/lfu-cache/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

#  Design and implement a data structure for a Least Frequently Used (LFU) cache.
#  Implement the LFUCache class:

    # LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    # int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    # void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
    # To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
# The functions get and put must each run in O(1) average time complexity.

class Node:

    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LFUNode:

    def __init__(self, freq=0, prev=None, next=None):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        return self.head.next == self.tail


class LFUCache_LL:

    def __init__(self, capacity: int):
        self.head = LFUNode()
        self.tail = LFUNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.nodeToLFUNode = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.addFreq(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.addFreq(node)
        else:
            node = Node()
            node.key = key
            node.val = value
            if self.addNewEntry(node):
                self.map[key] = node

    def addFreq(self, node):
        lfuNode = self.nodeToLFUNode[node]

        if lfuNode.next.freq != lfuNode.freq + 1:
            self.addNewLFUNode(lfuNode, lfuNode.freq + 1)

        isEmptyNode = lfuNode.removeNode(node)
        lfuNode.next.addNode(node)
        self.nodeToLFUNode[node] = lfuNode.next

        if isEmptyNode:
            self.removeLFUNode(lfuNode)

    def addNewEntry(self, node):
        if self.capacity == 0:
            return False

        if self.size == self.capacity:
            self.removeLeastFrequent()
        else:
            self.size += 1

        if self.head.next == self.tail or self.head.next.freq != 1:
            self.addNewLFUNode(self.head, 1)

        self.head.next.addNode(node)
        self.nodeToLFUNode[node] = self.head.next
        return True

    def addNewLFUNode(self, prev, freq):
        lfuNode = LFUNode()
        lfuNode.freq = freq
        lfuNode.next = prev.next
        lfuNode.prev = prev
        lfuNode.next.prev = lfuNode
        prev.next = lfuNode

    def removeLeastFrequent(self):
        lfuNode = self.head.next
        node = lfuNode.head.next
        isEmptyNode = lfuNode.removeNode(node)
        del self.map[node.key]
        del self.nodeToLFUNode[node]
        if isEmptyNode:
            self.removeLFUNode(lfuNode)

    def removeLFUNode(self, lfuNode):
        lfuNode.next.prev = lfuNode.prev
        lfuNode.prev.next = lfuNode.next


from collections import defaultdict, OrderedDict
# fre2od --> frequency to order
# minfre --> Min frequency
# key2fre --> key to freq
class LFUCache:
    def __init__(self, capacity: int):

        self.cap = capacity
        self.fre2od = defaultdict(OrderedDict)
        self.minfre = 0
        self.key2fre = {}

    # get function from LFU cache
    def get(self, key: int) -> int:

        # if key is not part of key2fre dict, return -1
        if key not in self.key2fre:
            return -1

        # if key is part of freq dict
        # pick freq & value for respective freq
        fre = self.key2fre[key]
        val = self.fre2od[fre][key]

        # pop the key from freq to order against old frequence
        # increase the freq and add it back in freq to order dict
        # update freq into key to freq dict
        # by default it moves the passed key to the end of the dictionary.
        self.fre2od[fre].pop(key)
        self.fre2od[fre + 1][key] = val
        self.key2fre[key] = fre + 1

        # if no element lfet in key's current freq and its same as min freq
        # increase min freq by 1
        if len(self.fre2od[fre]) == 0 and self.minfre == fre:
            self.minfre = fre + 1

        # return val
        return val

    # put function in LFU cache
    def put(self, key: int, val: int) -> None:

        # if key is not in key to freq dict
        # add in key2fre and fre2od dict
        if key not in self.key2fre:
            if self.cap == 0:
                if len(self.fre2od[self.minfre]) == 0:  # corner case,means initial capacity is zero,cap cannot be freed.
                    return
                # delete the least fre used element from LFU
                # Passing True to the method or passing no argument deletes the last item and passing False deletes the first item of the OrderedDict
                # passing false as LFU is present at first location of the dict
                delKey, _ = self.fre2od[self.minfre].popitem(last=False)
                del self.key2fre[delKey]
                # increase capacity by 1 after deleting an element
                self.cap += 1

            # reduce the capcity of cache
            # update key2freq & key2od dict
            # set min freq to 1 as this is a new element
            self.cap -= 1
            self.key2fre[key] = 1
            self.fre2od[1][key] = val
            self.minfre = 1

        # if already present , update the value and update the freq
        else:
            fre = self.key2fre[key]
            self.fre2od[fre][key] = val  # update val
            self.get(key)  # update fre

def main():

    lfu = LFUCache(3)
    lfu.put(1,10)
    print(lfu.fre2od , lfu.key2fre)
    lfu.put(2, 20)
    print(lfu.fre2od, lfu.key2fre)
    lfu.put(3, 30)
    print(lfu.fre2od, lfu.key2fre)
    lfu.put(4, 40)
    print(lfu.fre2od, lfu.key2fre)
    res= lfu.get(3)
    print(res)
    print(lfu.fre2od, lfu.key2fre)
    res = lfu.get(2)
    print(res)
    print(lfu.fre2od, lfu.key2fre)
    res = lfu.get(4)
    print(res)
    print(lfu.fre2od, lfu.key2fre)
    lfu.put(5, 50)
    print(lfu.fre2od, lfu.key2fre)

if __name__ == '__main__':
    main()