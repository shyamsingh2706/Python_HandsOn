# https://leetcode.com/problems/contains-duplicate-iii/

# Given an integer array nums and two integers k and t, return true if
# there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.


class Solution:

    # Brute force solution is use two loops and test both the conditions.
    # The inner loop starts from i+1 to i+k.
    # Because of that, we no longer need to test one of the conditions since that is taken care of automatically.
    # Time complexity : O(n * k).
    # Space complexity : 0(n)
    def containsNearbyAlmostDuplicate_BF(self, nums, k, t):

        n = len(nums)
        if t < 0:
            return False

        # if t = 0 and all numbers in num array is unique, return false.
        if t == 0 and len(set(nums)) == n :

            return False

        for i in range(n):
            for j in range(i + 1, i + k + 1):
                if j >= n:
                    break
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    # Buckets Method

    # Maintain buckets each of size t+1 holding the last k elements. This is the invariant.
    # Buckets are [0, t], [t+1,2t+1], [2t+2, 3t+2],....
    # What are the conditions of a match? Either x lies in a bucket which already has a member (this directly means that x and this element are within t of each other). Or the two neighbors of around this bucket may have a potential match. Check the code for an explanation.
    # Lastly we notice how we purge elements from the cache/buckets which are stale i.e. outside the window of k elements.
    # Notice one more thing: -3//5 = -1 - Python does this automatically and hence we dont need any special magic for handling negative numbers.

    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if t < 0:
            return False
        cache = {}
        for i in range(len(nums)):
            if i - k > 0:
                bucket_id_to_delete = nums[i - k - 1] // (t + 1)
                del cache[bucket_id_to_delete]
            bucket_id = nums[i] // (t + 1)
            condition1 = (bucket_id in cache)
            condition2 = ((bucket_id - 1 in cache and abs(cache[bucket_id - 1] - nums[i]) <= t))
            condition3 = ((bucket_id + 1 in cache and abs(cache[bucket_id + 1] - nums[i]) <= t))
            if condition1 or condition2 or condition3:
                return True
            cache[bucket_id] = nums[i]
        return False


def main():

    arr =  [1,5,9,1,5,9]
    k= 2
    t = 3
    s = Solution()
    res = s.containsNearbyAlmostDuplicate(arr,k,t)
    print(res)
    res_bf = s.containsNearbyAlmostDuplicate_BF(arr, k, t)
    print(res_bf)


if __name__ == "__main__":
    main()