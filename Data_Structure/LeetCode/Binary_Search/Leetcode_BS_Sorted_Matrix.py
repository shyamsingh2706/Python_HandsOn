#https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

#Given an n x n matrix and a number x,
# find the position of x in the matrix if it is present in it.
# Otherwise, print “Not Found”.
# In the given matrix, every row and column is sorted in increasing order.
# The designed algorithm should have linear time complexity.


def BS_Sorted_matrix(arr,x):

    N = len(arr[0])
    start = 0
    end = N - 1

    # check for array bound and if breaking , means element not found
    while (start >= 0 and start < N and end >= 0 and end < N ) :
        # start from last index of first row
        # if matching , return the same
        if arr[start][end] == x :
            return start,end
        # if its greater than the key, transver to same row but previous column
        elif  arr[start][end] > x :
            end -= 1
        #if its less than the key, transverse to same column but next row.
        elif arr[start][end] < x:
            start+= 1
    # return - if not found
    return -1

def main():
    # Driver Code
    arr = [ [10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50]];
    
    x = 27

    print(" Element's Index Postion in Sorted Matrix is :", BS_Sorted_matrix(arr,x))

if __name__ == "__main__":

    main()