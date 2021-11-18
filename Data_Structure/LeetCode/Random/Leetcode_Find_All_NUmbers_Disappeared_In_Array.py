
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(arr: list[int]) -> list[int]:

    idx = 0
    while idx < len(arr):
        # arr[idx] - 1 --> proposed Index position for a given element in sorted array i.e. if element value is 2 then its index position will be arr[idx] - 1 i.e. 1
        # arr[arr[idx] - 1] -->  find the element sitting in this proposed index postion in sorted array i.e. if 1 is index postion , the element value should be 2 on this index
        if arr[arr[idx] - 1] != arr[idx]:  # if current element value is same as its proposed index location's value , go to next element
            # else swap the position
            temp = arr[arr[idx] - 1]
            arr[arr[idx] - 1] = arr[idx]
            arr[idx] = temp
        else:
            idx += 1

    res = []
    for idx in range(len(arr)):
        if idx + 1 != arr[idx]:
            res.append(idx + 1)

    return res

def main():
    arr = [4,3,2,7,8,2,3,1]
      #    1,2,3,4,5,6,7,8
    print(findDisappearedNumbers(arr))

if __name__ == "__main__":
    main()