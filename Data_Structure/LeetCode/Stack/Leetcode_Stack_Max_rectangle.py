# https://leetcode.com/problems/maximal-rectangle/

import Leetcode_Stack_Area_Of_histogram
import numpy as np

def max_rectangle(arr):

    arr_rows = len(arr) ## Findout number of rows in given Matrix
    arr_cols = len(arr[0])  ## Findout number of rows in given Matrix

    # if array is empty
    if arr_rows == 0 or  arr_cols == 0:
        return 0

    temp = []
    temp = np.full((arr_cols),0).tolist()
    #print(temp)
    max_rectangle_area = 0

    # read one rwo at a time and pass into Max Area of Histogram program to fet max area for that array
    # for consicutive rown, take sum of previous row with current row before passing it to MAH function
    # if any element is 0 , consider overall sum as 0 for that column as ractangle cannot be formed in such case
    for i in range(arr_rows) :
        for j in range(arr_cols):

            if arr[i][j] == 0 :
                temp[j] = 0
            else :
                temp[j] = ( arr[i][j] + temp[j] )

        #print(temp)
        max_rectangle_temp = Leetcode_Stack_Area_Of_histogram.Max_area_of_Histogram(temp)
        #print (max_rectangle_temp)
        max_rectangle_area = max(max_rectangle_area,max_rectangle_temp)

    return max_rectangle_area

def main():
    # Driver Code
    arr = [[1, 0, 1, 0, 0],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 0, 0, 1, 0]];

    print(" Max Rectangle Area of given Array is :", max_rectangle(arr))

if __name__ == "__main__":

    main()