# 76. Minimum Window Substring - HARD
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        countT, window = {}, {}
        for el in t:
            if el in countT:
                countT[el] += 1
            else:
                countT[el] = 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from left of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float('infinity') else ''
