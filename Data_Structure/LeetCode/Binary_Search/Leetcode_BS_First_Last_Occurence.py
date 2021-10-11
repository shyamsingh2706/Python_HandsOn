# https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/
# https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

# Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

def Binary_Search_first_Occur(arr,x,start,end):
    First_occur_index_pos = 0
    while end >= start :

       Mid_element = (start + end) // 2

       if arr[Mid_element] > x:
            end = Mid_element-1
       elif arr[Mid_element] < x:
            start = Mid_element+1
       else:
           # If arr[mid] is same as x, we
           # update res and move to the left half
            end = Mid_element - 1
            First_occur_index_pos = Mid_element

    return First_occur_index_pos

def Binary_Search_Last_Occur(arr,x,start,end):

    Last_occur_index_pos = 0
    while end >= start :

       mid_element = (start + end) // 2
       if arr[mid_element] > x:
            end = mid_element-1
       elif arr[mid_element] < x:
            start = mid_element+1
       else:
           # If arr[mid] is same as x, we
           # update res and move to the Right half
           start = mid_element + 1
           Last_occur_index_pos = mid_element

    return Last_occur_index_pos

def main():
    # Driver Code
    arr = [2,2,2,4,10,10,10,11,20,20]
    x = 20

    print("First occurence is : " , Binary_Search_first_Occur(arr, x, 0, len(arr) - 1))
    print("Last occurence is : ", Binary_Search_Last_Occur(arr, x, 0, len(arr) - 1))
    print("Count of occurence is : ", Binary_Search_Last_Occur(arr, x, 0, len(arr) - 1) - Binary_Search_first_Occur(arr, x, 0, len(arr) - 1) + 1 )
if __name__ == "__main__":

    main()