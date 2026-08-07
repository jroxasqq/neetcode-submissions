class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # the distinct character in the longest substring is the most frequent
        # char of that window. This is because if you think about it greedily,
        # relative to all other char of the window, it will have as much, if not
        # less, replacements needed to form the longest substring.
        freqs, highest = dict(), float("-inf")
        left, right = 0, 0
        longest = float("-inf")

        # iterating char-by-char left to right of string s.
        while right < len(s):
            freqs[s[right]] = freqs.get(s[right], 0) + 1

            # we update highest frequency of the current char (s[right]) has highest
            # frequency than the running highest. This allows for constant time update
            # of the highest frequency, thus is most efficient.
            highest = max(highest, freqs[s[right]])

            window_size = right - left + 1

            # the number of replacement in the window should be at most k and is equal
            # to (current window size - frequency of highest frequenct char). 
            # Incrementing the left index by one is equivalent to removing it from
            # the window.
            if window_size - highest > k:
                freqs[s[left]] -= 1
                left += 1
                window_size -= 1

            longest = max(longest, window_size)
            right += 1

        return longest        
