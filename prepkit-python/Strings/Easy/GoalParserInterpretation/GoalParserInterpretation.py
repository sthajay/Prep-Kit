# 1678. Goal Parser Interpretation
# My Solution: https://leetcode.com/problems/goal-parser-interpretation/solutions/3577090/using-dict-no-need-to-hardcode/

class Solution:
    def interpret(self, command: str) -> str:

        obj = {'G': 'G', '()': 'o', '(al)': 'al'}

        for k, v in obj.items():
            command = command.replace(k, v)
        return command

        # Other Solution
        # While loop
        # ans = ''
        # p1 = 0
        # while p1 < len(command):
        #     if command[p1] == '(' and command[p1 + 1] == ')':
        #         ans = ans + 'o'
        #         p1 += 2

        #     elif command[p1] == '(' and command[p1+1] != ')':
        #         ans = ans + 'al'
        #         p1 += 4
        #     else:
        #         ans = ans + command[p1]
        #         p1 += 1
        # return ans

    # For Loop
        # ans = ''
        # for p1 in range(len(command)):
        #     if command[p1] == ')' or command[p1] == 'a' or command[p1] == 'l':
        #         continue

        #     if command[p1] == '(' and command[p1 + 1] == ')':
        #         ans = ans + 'o'

        #     elif command[p1] == '(' and command[p1+1] != ')':
        #         ans = ans + 'al'

        #     else:
        #         ans = ans + command[p1]
        # return ans
