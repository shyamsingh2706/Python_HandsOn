# Given an array of letters sorted in ascending order,
# find the smallest letter in the the array which is greater than a given key letter.


def BS_next_Alphabetical_element(arr,x,start,end):

    result = "#"

    while end >= start :

        mid_element = ( start + end ) //2
        if arr[mid_element] == x:
            ## as we need to find out greate element only. Continue the search in right direction.
            start = mid_element+1
        elif arr[mid_element] > x:
            end = mid_element-1
            ## If and element is greater than X , means it can be a possible floor value, store it
            result = arr[mid_element]
        elif arr[mid_element] < x:
            start = mid_element+1


    return result

#Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x,
# Assume than the array is sorted in Ascending order.


def main():
    # Driver Code
    arr = ['a','c','f','h']
    x = 'f'

    Floor = BS_next_Alphabetical_element(arr, x, 0, len(arr) - 1)

    print("Floor Element :", Floor)

if __name__ == "__main__":

    main()