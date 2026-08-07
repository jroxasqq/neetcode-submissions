class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars_in_window = set()
        longest = 0
        while right < len(s):

            # Keep shift left boundaries of window until there's no duplicates
            while s[right] in chars_in_window:
                chars_in_window.remove(s[left])
                left += 1

            longest = max(longest, right - left + 1)

            chars_in_window.add(s[right])

            print(s[left:right])
            right += 1

        return longest