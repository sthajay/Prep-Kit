# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        max_profit = 0
        for p2 in range(1, len(prices)):
            if prices[p2] < prices[p1]:
                p1 = p2
            else:
                diff = prices[p2] - prices[p1]
                if diff > max_profit:
                    max_profit = diff
        return max_profit

    # Other Solution
        # p1 = 0
        # max_profit = 0
        # for p2 in range(1, len(prices)):
        #     if prices[p2] < prices[p1]:
        #         p1 = p2
        #     else:
        #         max_profit = max(max_profit, prices[p2] - prices[p1])
        # return max_profit
