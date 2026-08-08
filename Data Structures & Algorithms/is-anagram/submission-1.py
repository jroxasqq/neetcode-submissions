class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freqs, t_freqs = dict(), dict()
        
        for c in s:
            s_freqs[c] = s_freqs.get(c, 0) + 1
        
        for c in t:
            t_freqs[c] = t_freqs.get(c, 0) + 1

        if len(s_freqs.keys()) != len(t_freqs.keys()):
            return False

        for c in s_freqs.keys():
            if s_freqs[c] != t_freqs.get(c, 0):
                return False

        return True
        

