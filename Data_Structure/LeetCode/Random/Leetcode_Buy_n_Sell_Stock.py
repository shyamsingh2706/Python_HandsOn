# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# similar to smaller element to left


class Solution():
    def maxProfit(self,arr):

        maxProfit = 0
        min = arr[0]
        for i in arr:
            if i < min:
                min = i
            else:
                maxProfit = max(maxProfit, i - min)

        return maxProfit

def main() :

    arr = [1,4,1,4,3,1]
    s = Solution()
    nxt_smaller_element_R  = s.maxProfit(arr)
    print ( "max Profit is  : ", nxt_smaller_element_R)
if __name__ == "__main__":
    main()