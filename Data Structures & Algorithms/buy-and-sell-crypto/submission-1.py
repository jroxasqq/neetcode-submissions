class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_lowest = float("inf")
        for i in range(len(prices)):
            curr_lowest = min(curr_lowest, prices[i])
            max_profit = max(max_profit, prices[i] - curr_lowest)

        return max_profit