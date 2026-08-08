class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the partner to nums[i] is target - nums[i].
        # partners is a dict of { partner : index of partner }
        partners = dict()
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in partners:
                return [partners[partner], i]
            partners[nums[i]] = i
        
        raise RuntimeError("one pair of indices was assumed to exist.")