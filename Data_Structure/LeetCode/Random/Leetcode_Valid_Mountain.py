# https://leetcode.com/problems/valid-mountain-array

# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# another appraoch 
class Solution:

    def validMountainArray(self, arr: list[int]) -> bool:

        decreasing = False
        has_increased = False
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                has_increased = True
                if decreasing:
                    return False
            elif arr[i] < arr[i - 1]:
                if not decreasing:
                    decreasing = True
            else:
                # arr[i] is equal to arr[i-1]
                return False

        return has_increased == True and decreasing == True


class Solution_other:
    def validMountainArray(self, arr: list[int]) -> bool:

        n = len(arr)

        # Is not a mountain if the length is less than 3 and
        # If the mountain starts descending from start
        if n < 3 or arr[0] > arr[1]:
            return False

        # Flag to detect when is ascending or descending
        isGrow = True
        last = arr[0]

        # We start from 1 to n - 1
        for ind in range(1, n):

            cur = arr[ind]

            # There can not be repeated numbers
            if last == cur:
                return False

            # When the mountain is growing there is a time when you reach the peek and start descending
            if isGrow and last > cur:
                isGrow = False

            # When the mountain is descending and de current number is greater than the last
            if not isGrow and cur > last:
                return False

            last = cur

        # The mountain should descend at least  once
        return not isGrow


def main():
    arr = [0, 1, 2, 1, 2]
    s = Solution()
    print(s.validMountainArray(arr))


if __name__ == "__main__":
    main()