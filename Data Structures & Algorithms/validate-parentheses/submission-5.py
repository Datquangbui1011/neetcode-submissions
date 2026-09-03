class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pair = {"()", "{}", "[]"}
        for i in s:
            if i in '([{':
                stack.append(i)
            elif not stack or stack.pop() + i not in valid_pair:
                return False
        return not stack
