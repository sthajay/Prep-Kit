# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el == '+':
                stack.append(stack.pop() + stack.pop())
            elif el == '*':
                stack.append(stack.pop() * stack.pop())
            elif el == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif el == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(el))
        return stack[0]

        # Other Solution
        # stack = []
        # ans = 0
        # for el in tokens:
        #     if el.isdigit():
        #         stack.append(int(el))
        #     elif len(el) > 1 and el[0] == '-' and el[1:].isdigit():
        #         stack.append(int(el))
        #     else:
        #         if len(stack) > 1:
        #             a = stack.pop()
        #             b = stack.pop()
        #             if el == '+':
        #                 ans = a + b
        #             elif el == '-':
        #                 ans = b - a
        #             elif el == '*':
        #                 ans = a * b
        #             else:
        #                 ans = int(b / a)
        #             stack.append(ans)
        # return stack[0]
