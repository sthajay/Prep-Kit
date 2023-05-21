# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = []
        for i in range(len(accounts)):
            total.append(sum(accounts[i]))
        return max(total)

    # Other Solution
    # return max([sum(el) for el in accounts])

    # return max(sum(el) for el in accounts)
