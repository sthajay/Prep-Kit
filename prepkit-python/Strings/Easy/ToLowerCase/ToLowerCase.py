# 709. To Lower Case
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ''
        for el in s:
            if 65 <= ord(el) <= 90:
                ans += chr(ord(el) + 32)
            else:
                ans += el
        return ans
