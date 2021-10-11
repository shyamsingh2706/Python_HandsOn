
# Given a sorted array, find the element in the array
# which has minimum difference with the given number.

import Leetcode_BS_Ceil_Floor_Values

def BS_Min_Diff_Element(arr,x):

    start = 0
    end = len(arr)-1

    floor = Leetcode_BS_Ceil_Floor_Values.BS_Floor_Soreted_Array(arr,x,start,end)
    ceil = Leetcode_BS_Ceil_Floor_Values.BS_Ceil_Soreted_Array(arr, x, start, end)


    if abs(x-ceil) > abs(x-floor):
        return floor
    else:
        return ceil


def main():
    # Driver Code
    arr = [1,6,7,10]
    x = 11

    Element = BS_Min_Diff_Element(arr,x)
    print(" Element with Minimum Difference in Sorted array is :", Element)

if __name__ == "__main__":

    main()