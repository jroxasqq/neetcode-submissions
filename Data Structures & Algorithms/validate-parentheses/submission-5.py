class Solution:
    def doesNotClose(self, closing, popped):
        if closing == ")":
            return not popped == "("
        elif closing == "}":
            return not popped == "{"
        elif closing == "]":
            return not popped == "["
        
        raise RuntimeError("arguement should be a closing bracket.")

    # for every open bracket, add to brackets.
    # for every closed bracket, check correct corresponding open bracket
    # at the end check no brackets remain (all open-closed pairs done)
    def isValid(self, s: str) -> bool:
        isOpen = lambda c: c == "(" or c == "{" or c == "["

        brackets = [] # list for our stack
        for c in s:
            if isOpen(c):
                brackets.append(c)
            else:
                if len(brackets) == 0 or self.doesNotClose(c, brackets.pop()):
                    return False

        return len(brackets) == 0

        