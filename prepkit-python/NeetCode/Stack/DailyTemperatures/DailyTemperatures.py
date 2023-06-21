# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, el in enumerate(temperatures):
            while stack and el > stack[-1][0]:
                stackEl, stackInd = stack.pop()
                ans[stackInd] = i - stackInd
            stack.append([el, i])
        return ans
