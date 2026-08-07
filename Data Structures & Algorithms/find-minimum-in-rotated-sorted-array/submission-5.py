class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search for the delection point index.
        left, right = 0, len(nums) - 1
        while True:
            mid = (left + right) // 2
            if nums[left] > nums[mid] < nums[right]:
                right = mid
            elif nums[left] < nums[mid] > nums[right]:
                left = mid
            else:
                return min(nums[left], nums[right])

        raise Exception("This should be unreachable, loop shoud've returned.")
