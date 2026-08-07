class Solution:
    # binary search on ascending ordered nums.
    def binary_search(self, nums: List[int], left: int, right: int, target: int):
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                # target == nums[mid]
                return mid

        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # binary search for the index of the deflection point of rotation.
        deflect = None
        while True:
            mid = (left + right) // 2
            if nums[left] > nums[mid] < nums[right]:
                right = mid
            elif nums[left] < nums[mid] > nums[right]:
                left = mid
            else:
                # nums[left] < nums[mid] < nums[right]
                deflect = left if nums[left] < nums[right] else right
                break

        # binary search left and right of the deflection index for the target.
        left_search = self.binary_search(nums, 0, deflect - 1, target)
        right_search = self.binary_search(nums, deflect, len(nums) - 1, target)

        # return the index if actually exists in nums.
        if left_search != -1:
            return left_search
        elif right_search != -1:
            return right_search
        return -1


