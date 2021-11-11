# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.


class Solution():
    def maxProfit(self,arr):

        if arr is None or len(arr) < 2:
            return 0

        maxProfit = 0
        for i in range(len(arr)-1):
            if arr[i+1] > arr[i]:
                maxProfit = maxProfit + (arr[i+1]-arr[i])

        return maxProfit

def main() :

    arr = [7,1,5,3,6,4]
    s = Solution()
    nxt_smaller_element_R  = s.maxProfit(arr)
    print ( "max Profit is  : ", nxt_smaller_element_R)
if __name__ == "__main__":
    main()