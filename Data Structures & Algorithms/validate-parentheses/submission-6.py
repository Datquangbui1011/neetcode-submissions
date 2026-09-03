class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pair = {"()", "[]", "{}"}
        for char in s:
            if char in '([{':
                stack.append(char)
            elif not stack or stack.pop()+char not in valid_pair:
                return False
        return not stack

        
        