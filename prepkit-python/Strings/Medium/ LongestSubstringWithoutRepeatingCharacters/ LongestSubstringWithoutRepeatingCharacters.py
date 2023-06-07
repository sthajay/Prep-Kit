# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        output = 0
        obj = {}
        if len(set(s)) == 1:
            return 1
        for p2 in range(len(s)):
            if s[p2] in obj:
                if obj[s[p2]] < p1:
                    diff = p2 - p1 + 1
                    if output < diff:
                        output = diff
                else:
                    p1 = obj[s[p2]] + 1
            else:
                diff = p2 - p1 + 1
                if output < diff:
                    output = diff
            obj[s[p2]] = p2
        return output
