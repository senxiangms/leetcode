""" You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7

Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3. """

#对1次交易， 2次交易， 三次， k次交易分别计算每个股票价格位置的获利
#两次交易是特殊情况
#对每一个价格， 有两个选择， 选择持股不动， 手里现金为上一个价格的hold， 或者买入， 上轮交易获利减去当前价格
#对每个价格， 当前获利， 是前一个价格的获利， 或者卖出hold+price[i]
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if 2*k >= len(prices): 
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
        
        pnl = [0]*len(prices)
        
        for _ in range(k):
            hold = -prices[0]
            for i in range(1, len(prices)):
                old = pnl[i]
                pnl[i] = max(pnl[i-1], hold+prices[i])
                hold = max(hold, old-prices[i])
        return pnl[-1]