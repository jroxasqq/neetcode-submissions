class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sum_pair = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                if total not in sum_pair:
                    sum_pair[total] = []
                sum_pair[total].append((i, j))
    
        result = set()
        for k in range(len(nums)):
            target = -nums[k]
            if target in sum_pair:
                for pair in sum_pair[target]:
                    i, j = pair
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    not_duplicate = triplet not in result
                    if k != i and k != j:
                        result.add(triplet)

        return [list(triplet) for triplet in result]