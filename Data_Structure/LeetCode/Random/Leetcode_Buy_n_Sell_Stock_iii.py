# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/327328/Python-Easy-to-understand

# devide and Concur Approach
# break array in 2 part and calculate max profit for each part
# sum up both profilt
# calculate maximum from each iteration
# Time Complixity O(n2) and Space Complixity O ( 1 )
import sys

import numpy as np
class Solution():
    def maxProfit_DivCon(self,arr):

        n = len(arr)
        if n < 2 :
            return 0

        maxProfit = 0
        profit = 0
        for k in range(n):
            profit_dev = 0
            profit_con = 0
            min_dev = arr[0]
            min_con = arr[k]
            for i in range(k):

                if arr[i] < min_dev:
                    min_dev = arr[i]
                else:
                    profit_dev = max(profit_dev, arr[i] - min_dev)

            for j in range(k,n):

                if arr[j] < min_con:
                    min_con = arr[j]
                else:
                    profit_con = max(profit_con, arr[j] - min_con)

            profit = profit_dev + profit_con
            maxProfit = max(maxProfit,profit)

        return maxProfit

    ## through DP
    def maxProfit_DP(self, prices: list[int]) -> int:

        if not prices:
            return 0

        k = 2
        dp_rows = k + 1 # rows
        dp_cols = len(prices) # columns
        dp = np.full((dp_rows, dp_cols), 0).tolist()

        print(dp)
        for k in range(1, dp_rows):
            min_p = prices[0]
            for i in range(1, dp_cols):
                # same approach as single transaction leetcode
                # i.e. first find min element and then minus that min element with current price
                # maximize the difference
                min_p = min(min_p, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - min_p)

        print(dp)
        return dp[-1][-1]

    ## through Loop , Time Complixity O(n) and Space Complixity O ( 1 )
    def maxProfit_loop(self, prices: list[int]) -> int:

        if len(prices) == 0 :
            return 0

        # as we need to maximize our profit
        # if we buy our stocks, we need to pay the money ( treat with minus sign )
        # if we sell our stock, difference of first buy and selling amount will be profit that we need to maximize
        # same applies for 2nd buy & 2nd sell
        first_buy = -sys.maxsize
        first_sell = 0

        second_buy = -sys.maxsize
        second_sell = 0

        for i in range(len(prices)):

            first_buy = max(first_buy,-prices[i])
            first_sell = max(first_sell, first_buy+prices[i])
            second_buy = max(second_buy, first_sell-prices[i])
            second_sell = max(second_sell, second_buy+prices[i])
            # Second Sell is our max profit

        return second_sell


def main() :

    arr = [1,2,3,4,5]
    s = Solution()
    nxt_smaller_element_R  = s.maxProfit_DP(arr)
    print ( "max Profit is  : ", nxt_smaller_element_R)
if __name__ == "__main__":
    main()