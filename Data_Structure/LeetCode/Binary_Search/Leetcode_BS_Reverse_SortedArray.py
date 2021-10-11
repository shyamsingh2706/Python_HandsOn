
# http://www.programming-algorithms.net/article/40119/Binary-search

def Reverse_Binary_Search(arr,x,start,end):

    mid_element = (start + end ) //2

    if len(arr) == 0 :
        return None

    if end >= start:
        if arr[mid_element] > x :
            return Reverse_Binary_Search(arr, x, mid_element+1, end)
        elif arr[mid_element] < x :
            return Reverse_Binary_Search(arr,x,start,mid_element-1)
        elif arr[mid_element] == x :
            return mid_element
    else:
        return None

def main():
    # Driver Code
    arr = [40,10,9,8,3,1]
    x = 10

    index = Reverse_Binary_Search(arr,x,0,len(arr)-1)

    print(index)

    if index != -1:
        print("Element is present at index :" , index)
    else:
        print("Element is not present in array")

if __name__ == "__main__":

    main()