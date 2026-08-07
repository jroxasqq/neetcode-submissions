class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars_in_window = set()
        longest = 0
        while right < len(s):

            # Keep shifting left boundary of window until the window no 
            # longer contains the duplicate value of s[right], i.e. the
            # s[left] may not necessarily be the duplicate value to
            # s[right] that we want to remove.
            while s[right] in chars_in_window:
                chars_in_window.remove(s[left])
                left += 1

            # The window bounded by left and right is non-inclusive of
            # s[right], so with +1 it's inclusive instead.
            longest = max(longest, right - left + 1)

            # Add s[right] to our window.
            chars_in_window.add(s[right])
            right += 1

        return longest