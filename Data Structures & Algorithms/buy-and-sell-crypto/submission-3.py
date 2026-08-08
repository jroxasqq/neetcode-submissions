class Solution:
    # consider that the best day to buy will always be the lowest value
    # before the day you sell so you keep trak of that (curr_lowest).
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_lowest = float("inf")
        for i in range(len(prices)):

            # best day to buy updated if better than before.
            curr_lowest = min(curr_lowest, prices[i])

            # max_profit updated is sell day is better than before.
            max_profit = max(max_profit, prices[i] - curr_lowest)

        return max_profit