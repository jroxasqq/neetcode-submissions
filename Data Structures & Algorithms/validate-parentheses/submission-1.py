class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if c == ")" and popped != "(":
                    return False
                if c == "}" and popped != "{":
                    return False
                if c == "]" and popped != "[":
                    return False

        return len(stack) == 0