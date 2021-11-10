# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# https://leetcode.com/problems/missing-number/
# https://leetcode.com/problems/find-the-duplicate-number/

# sapce complexity O(n)
# time complxity O(n)
import collections


def printTwoElements_Using_Dict(arr):

    # here this approach is using o(n) space while creating the Dict
    dict = collections.Counter(arr)

    # as 1 to N condition is defined , we can always use that to loop the array
    for i in range(1,len(arr)+1):
        if i in dict.keys():
            if dict[i] != 1:
                print("Duplicate Number is ", i)
                continue
        else:
            print("missing Number is ", i)


# 2nd approach using Mathmatics find the same in O(1) space complexity
# ideal arr = a,b,c,d,e   given arr = a,e,c,d,e
# Eq : 1 --> ideal_arr - given arr = b - e
# Eq : 2 --> a^2 + b^2 + c^2 + d^2 + e^2 - ( a^2+e^2+c^2+d^2+e^2 ) = b^2-e^2
# Eq1 / Eq2 = b+e --> Eq 3
# user Eq1 & eq 3 to find out missing number and duplicate number
# This method can cause arithmetic overflow as we calculate product and sum of all array elements.
# difficult to scale up if there are multiple missing and duplicate

# Approach 3  Time complexity O(n) and space complexit O(1)
#Traverse the array. While traversing, use the absolute value of every element as an index
# and make the value at this index as negative to mark it visited.
# If something is already marked negative then this is the repeating element. To find missing, traverse the array again and look for a positive value.

def printTwoElements(arr):

    size = len(arr)
    for i in range(size):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            print("The repeating element is", abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            print("and the missing element is", i + 1)

# Approach 4  using Swap sort .. Time Complexity O(n) and space complexit O(1)
# PS : if read only array has been given , this approach wont work

 # if we know the length of array in advance ,
# I can assume that if my array is sorted , the index postion + 1 will be the value of elements in array

# i.e. 1,2,3,4,5 will be at index position of 0,1,2,3,4
# so first we try to sort the array on this theory i.e. if a given element is not matching with its index postion
# we will swap this element to its right index position
# if an element is already sitting in its right index position , move to next element.

def printTwoElements_swap_Sort(arr):

    idx = 0
    while idx < len(arr):
         # arr[idx] - 1 --> proposed Index position for a given element in sorted array i.e. if element value is 2 then its index position will be arr[idx] - 1 i.e. 1
         # arr[arr[idx] - 1] -->  find the element sitting in this proposed index postion in sorted array i.e. if 1 is index postion , the element value should be 2 on this index
        if arr[arr[idx] - 1] !=  arr[idx] : # if current element value is same as its proposed index location's value , go to next element
            # else swap the position
            temp = arr[arr[idx] - 1]
            arr[arr[idx] - 1] = arr[idx]
            arr[idx] = temp
        else:
            idx += 1

    for idx in range(len(arr)):
        if idx+1 != arr[idx]:
            print("The repeating/duplicate element is", arr[idx])
            print("The missing element is", idx+1)


def main():

    arr = [1,5,3,4,6,5]
    printTwoElements_swap_Sort(arr)

if __name__ == "__main__":
    main()