# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.
# For simplicity, assume that all bars have same width and the width is 1 unit.

# idea is , if we notice, rectangle can be formed only when the same height to left and right is available
# in order to find the same , we need to find nearest smaller to right index and Nearest smaller to Left Index
# These index should be our stop point.
# so width of rectangle should be right - left - 1
# if we multiple further with Associated arry i.e. W* H ( it contains Height of each tower )
# This will give us area of each rectage for every tower.
# the max from this area will be output as max area possible for a rectangle in a histogram

def nearest_smallest_right_index(arr):

    rstk = []
    dummy_index = len(arr) ## assuming next Histogram present at max Index + 1 postion is 0, thats out stopping point
    right_smallest_index_arr = []

    for i in range(len(arr)-1,-1,-1):

        if len(rstk) == 0:
            right_smallest_index_arr.append(dummy_index)
        elif len(rstk) > 0 and arr[i] > rstk[-1][0]:
            right_smallest_index_arr.append(rstk[-1][1])
        elif len(rstk) > 0 and arr[i] <= rstk[-1][0]:
            while len(rstk) > 0 and arr[i] <= rstk[-1][0]:
                rstk.pop()
            if len(rstk) == 0:
                right_smallest_index_arr.append(dummy_index)
            else:
                right_smallest_index_arr.append(rstk[-1][1])

        rstk.append([arr[i],i])

    return right_smallest_index_arr[::-1]

def nearest_smallest_left_index(arr):

    lstk = []
    dummy_index = -1 ## assuming next Histogram present at min postion ie. -1, thats out stopping point
    left_smallest_index_arr = []

    for i in range(0,len(arr),1):

        if len(lstk) == 0:
            left_smallest_index_arr.append(dummy_index)
        elif len(lstk) > 0 and arr[i] > lstk[-1][0]:
            left_smallest_index_arr.append(lstk[-1][1])
        elif len(lstk) > 0 and arr[i] <= lstk[-1][0]:
            while len(lstk) > 0 and arr[i] <= lstk[-1][0]:
                lstk.pop()
            if len(lstk) == 0:
                left_smallest_index_arr.append(dummy_index)
            else:
                left_smallest_index_arr.append(lstk[-1][1])

        lstk.append([arr[i], i])

    return left_smallest_index_arr

def Max_area_of_Histogram(arr):

    NSLI = nearest_smallest_left_index(arr)
    NSRI = nearest_smallest_right_index(arr)

    width_of_rectangle =  []
    area_of_rectangle = []
    #print("NSRI :" , NSRI)
    #print("NSLI : " , NSLI)
    for i in range(0,len(arr)):
        width_of_rectangle.append(NSRI[i] - NSLI[i] - 1 )

    #print("width_of_rectangle :",width_of_rectangle)
    #print("Array : " , arr)
    for j in range(0,len(arr)):
        area_of_rectangle.append(width_of_rectangle[j] * arr[j] )

    return max(area_of_rectangle)

def main():

    arr = [3, 1, 3, 2, 2]
    MAH = Max_area_of_Histogram(arr)
    print("Max Area of Rectangle in given Histogram is : ", MAH)

if __name__ == "__main__":
    main()
