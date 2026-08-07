class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqs = set(nums)

        longest = 0
        for num in uniqs:
            if num - 1 not in uniqs: # Only starting values
                counter = 0
                curr = num
                while curr in uniqs:
                    counter += 1
                    curr += 1
                longest = max(longest, counter)
        return longest
