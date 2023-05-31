# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = {'L': 0, 'R': 0}
        ans = 0
        for el in s:
            counter[el] += 1
            if counter['L'] == counter['R']:
                ans += 1
        return ans

    # Other Solution
        # return list(accumulate(1 if el == 'R' else -1 for el in s)).count(0)

        # flag = ans = 0
        # for el in s:
        #     flag += 1 if el == 'R' else -1
        #     if flag == 0: ans += 1
        # return ans
