# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        ans = 0
        obj = {}
        for p2 in range(len(s)):
            if s[p2] in obj:
                obj[s[p2]] += 1
            else:
                obj[s[p2]] = 1
            if p2 - p1 + 1 - max(obj.values()) <= k:
                ans = p2 - p1 + 1
            else:
                obj[s[p1]] -= 1
                p1 += 1
        return ans
