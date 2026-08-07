class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs, highest = dict(), float("-inf")
        left, right = 0, 0
        longest = float("-inf")

        while right < len(s):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            highest = max(highest, freqs[s[right]])

            window_size = right - left + 1

            if window_size - highest > k:
                freqs[s[left]] -= 1
                left += 1
                window_size -= 1

            longest = max(longest, window_size)
            right += 1

        return longest

        # the distinct character is the most frequent char of that window.
        
        # as we iterate char-by-char, we compare the current char frequency in the
        # window with the current frequency char to check if we need to update.

        # the number of replacement in the window should be at most k and is equal
        # to (current window size - frequency of most frequenct char).
