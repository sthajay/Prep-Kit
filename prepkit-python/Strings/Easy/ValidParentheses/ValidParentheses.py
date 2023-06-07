# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        front = '({['
        for el in s:
            if el in front:
                stack.append(el)
            else:
                if not stack:
                    return False
                if el == ')' and stack[-1] == '(':
                    stack.pop()
                elif el == '}' and stack[-1] == '{':
                    stack.pop()
                elif el == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack
