''' Program to replicate Hash function with collision handling in case of a clash with hash Key '''

import mmh3

class hash_table():

    ## initialize a Hash table
    def __init__(self):
        self.num_of_element = 10
        self.arr = [ [] for j in range(self.num_of_element)]

    ## Function to get a Hash Index for given Key
    def get_hash(self, key):

        index = mmh3.hash(key, 1) % self.num_of_element
        return  int (index)

    # Dunder method to set a key , value pair
    def __setitem__(self, key, value):

        index = self.get_hash(key)
        found = False

        # logic to handle collision scenario in case of Index clash due to same hash key output for multiple different Keys
        for idx,element in enumerate(self.arr[index]):
            if (len(element) == 2 and key == element[0]):
                self.arr[index][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[index].append((key, value))

    # Dunder method to fetch a key from hash table
    def __getitem__(self, key):

        index = self.get_hash(key)
        for idx, element in enumerate(self.arr[index]):
            if ( key == element[0]):
                return element[1]

    # Dunder method to delete a key from hash table
    def __delitem__(self, key):

        index = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[index]):
            if (len(element) == 2 and key == element[0]):
                self.arr[index].pop(idx)
                # Alternate option
                # del self.arr[index][idx]

if ( __name__ == '__main__' ) :

    h = hash_table()
    h['March 6'] = 30
    print(h.arr)
    h['March 6'] = 40
    print(h.arr)
    h['March 17'] = 10
    print(h.arr)
    h['March 8'] = 10
    print(h.arr)
    del h['March 8']
    print(h.arr)
    del h['March 17']
    print(h.arr)
    print(h['March 6'])