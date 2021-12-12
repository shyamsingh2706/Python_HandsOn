
# https://leetcode.com/problems/allocate-mailboxes/
# https://leetcode.com/problems/allocate-mailboxes/discuss/1513947/The-explanation-you've-been-waiting-for

# Optimized Approach through storing into Hashmap ( dict )
class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        l = len(houses)
        if k >= l:
            return 0

        houses.sort()

        results = {}

        def findResult(start, end, r):
            if end - start <= r:
                return 0
            if (start, end, r) in results:
                return results[(start, end, r)]

            if r == 1:  # Calculate total distance for one subarray
                left = start
                right = end - 1
                current_result = 0
                while left < right:
                    current_result += houses[right] - houses[left]
                    right -= 1
                    left += 1
            else:
                current_result = 2147483647
                for i in range(start + 1, end):
                    current_result = min(current_result, findResult(start, i, 1) + findResult(i, end, r - 1))

            results[(start, end, r)] = current_result
            return current_result

        return findResult(0, l, k)


def main():

    houses = [1,4,8,10,20]
    k = 3
    s = Solution()
    Min_dist = s.minDistance(houses,k)

    print("Min Ditance is :", Min_dist)

if __name__ == "__main__":

    main()
