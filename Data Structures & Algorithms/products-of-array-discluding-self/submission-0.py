class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first_k_prod = [1 for _ in range(len(nums) + 1)] # first_k_prod[3] is the product of the first 3 elements.
        last_k_prod = [1 for _ in range(len(nums) + 1)] # last_k_prod[4] is the product of the last 4 elements.
        for i in range(1, len(nums) + 1):
            first_k_prod[i] = first_k_prod[i - 1] * nums[i - 1]
            last_k_prod[i] = last_k_prod[i - 1] * nums[len(nums) - i]

        result = []
        for i in range(1, len(nums) + 1):
            result.append(first_k_prod[i - 1] * last_k_prod[len(nums) - i])

        return result
