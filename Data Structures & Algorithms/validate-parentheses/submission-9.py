class Solution:
    def isValid(self, s: str) -> bool:
        stack = []   # stack to store opening brackets
        pair = {")": "(", "]": "[", "}": "{"}   # map closing bracket -> matching opening bracket

        for i in s:   # iterate through each character in the string
            if i in pair:   # if the character is a closing bracket
                # check if stack is not empty and top of stack matches the corresponding opening bracket
                if stack and stack[-1] == pair[i]:
                    stack.pop()   # remove the matched opening bracket
                else:
                    return False  # mismatch or no opening bracket available
            else:
                stack.append(i)   # if it's an opening bracket, push it to the stack

        # if stack is empty, all brackets matched correctly
        return True if not stack else False