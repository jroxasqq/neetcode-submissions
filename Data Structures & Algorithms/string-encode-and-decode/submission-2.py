class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        # Since each word is at most 200 characters long, we can
        # store the length in 3 digits, along with the word itself.
        for s in strs:
            result += f"{len(s):03d}{s}"
        
        return result

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0

        # For each "{word length}{word}" we read the word length then extract
        # the word by getting the slice, the move on to the next word.
        while idx < len(s):
            word_len = int(s[idx:(idx + 3)])
            strs.append(s[(idx + 3):(idx + 3) + word_len])
            idx += word_len + 3

        return strs