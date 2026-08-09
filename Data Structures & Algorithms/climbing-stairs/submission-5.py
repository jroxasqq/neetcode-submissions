class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0] * (n + 1)
        for i in range(1, n + 1):
            if i == 1 or i == 2:
                results[i] = i
            else:
                results[i] = results[i - 1] + results[i - 2] 
        
        return results[n]