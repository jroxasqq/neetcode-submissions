class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # money[i] is the maximum amount of money ending at house i.
        money = [float("-inf")] * n

        for i in range(n):
            if i < 2:
                money[i] = nums[i]
            else:
                money[i] = max(money[i - 2], money[i - 3]) + nums[i]

        return money[-1] if n == 1 else max(money[-1], money[-2])