class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict()
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
                
        # # sort freqs by frequency descening.
        # freqs_desc = sorted(freqs.items(), key=lambda item: -item[1])
        # return [key for key, val in freqs_desc[:k]]

        # consider that any num can occur at most len(nums) times.
        groups = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            groups[freq].append(num)
        
        result = []
        for group in groups[::-1]:
            for num in group:
                result.append(num)
                if len(result) == k:
                    return result
    