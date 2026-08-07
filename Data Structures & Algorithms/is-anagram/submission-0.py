class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts, t_counts = {}, {}
        for c in s:
            s_counts[c] = s_counts.get(c, 0) + 1
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1

        if len(s_counts) != len(t_counts):
            return False
        
        for c in s_counts.keys():
            if (c not in t_counts) or (s_counts[c] != t_counts[c]):
                return False

        return True