# Given an infinite sorted array consisting 0s and 1s.
# The problem is to find the index of first ‘1’ in that array. As the array is infinite,
# therefore it is guaranteed that number ‘1’ will be present in the array.

#https://www.geeksforgeeks.org/find-index-first-1-infinite-sorted-array-0s-1s/

def BS_infinite_Array(arr):

    start = 0
    end = 1

    while  1 > arr[end]:
        start = end
        end = end * 2

    while end >= start :

        mid_element = ( start + end ) //2
        if arr[mid_element] == 1:
            ## to find first occurence , keep on moving left.
            result = mid_element
            end = mid_element -1
        elif arr[mid_element] > 1:
            end = mid_element-1
        elif arr[mid_element] < 1:
            start = mid_element+1


    return result

#Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x,
# Assume than the array is sorted in Ascending order.


def main():
    # Driver Code
    arr = [0,0,1,1,1,1,1,1,1,1,1,1,1,1]


    Floor = BS_infinite_Array(arr)

    print("First Occurence of 1 in Infinite array is :", Floor)

if __name__ == "__main__":

    main()