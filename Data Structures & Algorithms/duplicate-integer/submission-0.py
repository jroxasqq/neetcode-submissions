class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqs = set(nums)
        return len(nums) != len(uniqs)