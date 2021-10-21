
### Approach 1
def sort(array, index = 0, bigNumber = 0):

  if len(array) == index:
    return array

  elif bigNumber > array[index]:
    array[index - 1] = array[index]
    array[index] = bigNumber
    bigNumber = array[0]
    index = 0

  else:
    bigNumber = array[index]

  return sort(array, (index + 1), bigNumber)

# Another approach of recurssion
# Approach 2 ( Sort Array or Stack in Ascending Order )
# same approach can be used for Stack also as
# we are using the start point from the last element of the array ( will be same for stack )

def sort_arr(arr):

    # length of array is 1, means array is already sorted
    if len(arr) == 1:
        return

    # if not, capture the last element of array
    # and sort the remaining array
    temp = arr[-1]
    del arr[-1]
    sort_arr(arr)

    # once remaining array is sorted, insert back the last element back to array
    # now insertion also is a recussion function
    insert_arr(arr, temp)


def insert_arr(arr,temp_insert):

    # while inserting into array , the base condition wil be
    # if array is empty or the element we are trying to insert it greater than last element of sorted array
    if len(arr) == 0 or arr[-1] <= temp_insert:
        # if yes , append it in the end of array
        arr.append(temp_insert)
        return

    # else reduce the array by 1 element and call insert function again on smaller array size i.e. without last element
    val = arr[-1]
    del arr[-1]
    insert_arr(arr,temp_insert)
    # once its inserted, insert back the value the we popped before calling insert function
    arr.append(val)

# Sort Array in descending Order

def sort_arr_desc(arr):

    # length of array is 1, means array is already sorted
    if len(arr) == 1:
        return

    # if not, capture the last element of array
    # and sort the remaining array
    temp = arr[0]
    del arr[0]
    sort_arr_desc(arr)

    # once remaining array is sorted, insert back the last element back to array
    # now insertion also is a recussion function
    insert_arr_desc(arr, temp)


def insert_arr_desc(arr,temp_insert):

    # while inserting into array , the base condition wil be
    # if array is empty or the element we are trying to insert it greater than last element of sorted array
    if len(arr) == 0 or arr[0] <= temp_insert:
        # if yes , append it in the end of array
        arr.insert(0,temp_insert)
        return

    # else reduce the array by 1 element and call insert function again on smaller array size i.e. without last element
    val = arr[0]
    del arr[0]
    insert_arr_desc(arr,temp_insert)
    # once its inserted, insert back the value the we popped before calling insert function
    arr.insert(0,val)



def main():

    global arr
    arr = [4,1,6,0,2,7,3]

    print("sorted array through recursion is Aproach 1 is ", sort(arr))

    sort_arr(arr)
    print("sorted array through recursion is Aproach 2 is " , arr )

    arr = [4, 1, 6, 0, 2, 7, 3]
    sort_arr_desc(arr)
    print("sorted array through recursion is Aproach 2 in DESC order is ", arr)


if __name__ == "__main__":
    main()
