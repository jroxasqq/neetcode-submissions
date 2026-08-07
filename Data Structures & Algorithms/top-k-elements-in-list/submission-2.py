class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict()
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        # consider that any num can occur at most len(nums) times.
        groups = [[] for _ in range(len(nums) + 1)]

        # groups[i] is the numbers with frequencies of i.
        for num, freq in freqs.items():
            groups[freq].append(num)
        
        # append the last k numbers from the groups.
        result = []
        for group in groups[::-1]:
            for num in group:
                result.append(num)
                if len(result) == k:
                    return result
    