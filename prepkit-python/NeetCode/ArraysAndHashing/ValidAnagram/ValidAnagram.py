# 242. Valid Anagram
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    # Other Solution
    # return sorted(s) == sorted(t) - 0(1) memory complexity
