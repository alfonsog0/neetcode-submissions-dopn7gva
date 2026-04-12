class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                parenthesis = ''
                parenthesis = stack[-1] + char
                if parenthesis == '{}' or parenthesis == '[]' or parenthesis == '()':
                    stack.pop()
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False