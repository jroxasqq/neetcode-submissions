class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if nums[i] in pair_idx.keys():
                smaller = min(i, pair_idx[nums[i]])
                larger = max(i, pair_idx[nums[i]])
                return [smaller, larger]
            pair_idx[pair] = i