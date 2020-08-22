from bitarray import bitarray
import mmh3
import numpy as np
import random

class BloomFilter():

    def __init__(self,num_of_element,probability):

        self.num_of_element = num_of_element
        self.probability = probability

        # determine size of array to store number of element
        self.size = self.check_size(self.num_of_element,self.probability)
        # Determine Optimum number of hash functions needed for input probability
        self.hash_fn_count = self.hash_needed(self.size,self.num_of_element)

        # intialize Bitarray

        self.arr = bitarray(self.size)
        self.arr.setall(0)

    def add_element(self,element_name):

        # create an array for given item.
        # j work as seed to mmh3.hash() function
        # With different seed, array created is different

        sub_list= []
        for j in range(self.hash_fn_count):
            index = mmh3.hash(element_name,j) % self.size
            sub_list.append(index)
            self.arr[index] = True

    def check_element(self,element_name):
        # Check  for existence of an item in filter
        for j in range(self.hash_fn_count):
            index = mmh3.hash(element_name,j) % self.size
            if (self.arr[index] == True):
                return True
            else:
                return False

    def check_size(self,no_of_ele,prob):

        '''Size of Bit Array: If expected number of elements n is known and desired false positive probability is p then the size of bit array m can be calculated as :

        m= - {n * ln P}/ {(ln 2)^2}
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        '''

        arr_size = - (no_of_ele * np.log(prob)) / (np.square(np.log(2)))
        return int(arr_size)


    def hash_needed(self, arr_size, no_of_ele):
        '''
        Optimum number of hash functions: The number of hash functions k must be a positive integer.
        If m is size of bit array and n is number of elements to be inserted, then k can be calculated as :

        k = (m/n) * ln2

        '''

        hash = (arr_size/no_of_ele) * np.log(2)
        return int(hash)

if ( __name__ == '__main__' ) :

    '''
    n = 20  # no of items to add 
    p = 0.05  # false positive probability 
    '''

    BlmFltr = BloomFilter(20,0.05)
    print("Size of bit array:{}".format(BlmFltr.size))
    print("Number of hash functions:{}".format(BlmFltr.hash_fn_count))

    # words to be added
    word_to_be_added = ['abound', 'abounds', 'abundance', 'abundant', 'accessable',
                    'bloom', 'blossom', 'bolster', 'bonny', 'bonus',
                    'coherent', 'cohesive', 'colorful', 'comely', 'comfort',
                    'gems', 'generosity', 'generous', 'generously', 'genial']

    # word not added
    word_to_be_missed = ['bluff', 'cheater', 'hate', 'war', 'humanity',
                   'racism', 'hurt', 'nuke', 'gloomy', 'facebook',
                   'geeksforgeeks', 'twitter']

    random.shuffle(word_to_be_added)
    random.shuffle(word_to_be_missed)

    print(f"word_to_be_added is {word_to_be_added}")
    print(f"word_to_be_missed is {word_to_be_missed}")

    for item in word_to_be_added :
        BlmFltr.add_element(item)

    validate_word_list = word_to_be_added[:10] + word_to_be_missed
    random.shuffle(validate_word_list)
    print(f"validate_word_list is {validate_word_list}")

    for item in validate_word_list :
        if (BlmFltr.check_element(item) == True):
            if item in word_to_be_missed :
                print (f"{item} is false positive !! ")
            else:
                print (f"{item} is probably present !! ")
        else:
            print(f"{item} is not present !! ")