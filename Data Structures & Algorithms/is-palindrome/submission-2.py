def getNextAlNum(s, curr_idx, idx_type):
    new_idx = curr_idx
    while 0 <= new_idx <= len(s) - 1 and not s[new_idx].isalnum():
        new_idx += 1 if idx_type == "start" else -1
    
    return new_idx

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start <= end:
            start = getNextAlNum(s, start, "start")
            end = getNextAlNum(s, end, "end")
            if start > end:
                break
            print(f"{s[start]}, {s[end]}")
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True