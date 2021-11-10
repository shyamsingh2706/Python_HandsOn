# https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    def containsNearbyDuplicate(self, arr: list[int], k: int) -> bool:

        dup_dict = {}
        for i in range(len(arr)):
            num = arr[i]
            if ((num in dup_dict.keys()) and abs(dup_dict[num] - i ) <= k ):
                return True

            dup_dict[num] = i
        return False

def main():

    arr =   [1,2,3,1,2,3]
    k= 2
    s = Solution()
    res = s.containsNearbyDuplicate(arr,k)
    print(res)

if __name__ == "__main__":
    main()