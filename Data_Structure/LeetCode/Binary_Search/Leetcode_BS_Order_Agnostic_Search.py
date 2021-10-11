## https://www.prodevelopertutorial.com/order-agnostic-binary-search/

# Given a sorted array of numbers
# find if a given number ‘key’ is present in the array.
# Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.

import Leetcode_BS_Binary_Search_Base
import Leetcode_BS_Reverse_SortedArray


def main():
    # Driver Code
    arr = [100,75,40,12,4,1]
    x = 4

    # find out if array of reverse sorted
    if arr[0] > arr[-1]:
        index = Leetcode_BS_Reverse_SortedArray.Reverse_Binary_Search(arr,x,0,len(arr)-1)
    else:
        index = Leetcode_BS_Binary_Search_Base.Binary_Search_iterative(arr,x,0,len(arr)-1)

    print(index)

if __name__ == "__main__":

    main()