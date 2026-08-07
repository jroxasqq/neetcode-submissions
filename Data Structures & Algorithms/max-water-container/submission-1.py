class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        maximum = float("-inf")
        while start < end:
            amount = min(heights[start], heights[end]) * (end - start)
            maximum = max(maximum, amount)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return maximum