""" You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
  """
#sold记录卖出的收益
#hold记录持有的收益
#rest记录休息获得收益
#对每一笔价格, 选择卖出， 可以获得sold = hold+price, 选择持有hold = max(hold, rest - price), 选择休息rest = max(rest, prevsold)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = -math.inf
        hold = -math.inf
        rest = 0
        for price in prices:
            prevsold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prevsold)
        return max(sold, rest)