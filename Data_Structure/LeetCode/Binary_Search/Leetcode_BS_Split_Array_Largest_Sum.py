
#https://www.geeksforgeeks.org/allocate-minimum-number-pages/

# Given number of pages in n different books and m students.
# The books are arranged in ascending order of number of pages.
# Every student is assigned to read some consecutive books.
# The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.


# similar problem #https://leetcode.com/problems/split-array-largest-sum/
# Given an array nums which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

import sys

def is_valid(arr,m,mid_element):

    sum = 0
    num_split = 1

    for i in arr:

        # check if current number of pages are
        # greater than curr_min that means
        # we will get the result after
        # mid no. of pages
        if (i > mid_element):
            return False

        # update curr_sum
        sum = sum + i
        # count how many students are required
        # to distribute curr_min pages
        if sum > mid_element:
            # update curr_sum
            sum = i
            # increment student count
            num_split += 1

    # if students required becomes greater
    # than given no. of students, return False
    if num_split > m :
        return False
    else :
        return True


def BS_Split_Arr_Largest_Sum(arr,m):

    # initialize start as 0 pages and
    # end as total pages
    start = 0
    end = sum(arr) # Count total number of pages
    largest_sum = sys.maxsize
    N = len(arr)

    # return -1 if no. of books is
    # less than no. of students
    if N < m:
        return -1

    while end >= start :
        # check if it is possible to distribute
        # books by using mid as current minimum
        mid_element =  (start + end) // 2

        if ( is_valid(arr,m,mid_element) == True):

            # update result to current distribution
            # as it's the best we have found till now.
            largest_sum = mid_element
            # as we are finding minimum and books
            # are sorted so reduce end = mid -1
            # that means move towards left to find another minimum if possible
            end = mid_element -1
        else:
            # if not possible means pages should be
            # increased so update start = mid + 1
            start = mid_element + 1

    return largest_sum

def main():

    arr = [1,2,3,4,5]
    m = 2

    Largest_Sum = BS_Split_Arr_Largest_Sum(arr,m)

    print("largest Sum possible for given array is :", Largest_Sum)

if __name__ == "__main__":

    main()