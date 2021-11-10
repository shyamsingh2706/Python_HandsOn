#  https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# time Complx : O(nLogn) , space Complxity O(1)
def containsDuplicate_sort(arr):

    arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True

    return False

# time Complx : O(n) , space Complxity O(n)
def containsDuplicate_set(arr):

    dup_set = set()

    for i in arr:
        if i in dup_set:
            return True
        dup_set.add(i)

    return False

def containsDuplicate(arr):
    return len(set(arr)) != len(arr)

def main():

    arr = [1,2,4,4,6,5]
    res = containsDuplicate(arr)
    print(res)

if __name__ == "__main__":
    main()