class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s):03d}{s}"
        return result

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        while idx < len(s):
            word_len = int(s[idx:(idx + 3)])
            strs.append(s[(idx + 3):(idx + 3) + word_len])
            idx += word_len + 3

        return strs