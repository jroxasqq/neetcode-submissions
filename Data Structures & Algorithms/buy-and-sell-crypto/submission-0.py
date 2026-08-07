class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_lowest = [] # running_lowest[3] is the lowest value up to and including index 3 (so first 4 elements).
        lowest = float("inf")
        for price in prices:
            lowest = min(lowest, price)
            running_lowest.append(lowest)
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - running_lowest[i])

        return max_profit