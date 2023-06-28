# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    # Other solution - 1 (Iterate through all the characters)
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if not s[l].isalnum():
        #         l += 1
        #     elif not s[r].isalnum():
        #         r -= 1
        #     elif s[l].lower() != s[r].lower():
        #         return False
        #     else:
        #         l += 1
        #         r -= 1
        # return True

    # Other Solution - 2
        # l, r = 0, len(s) - 1
        # while l < r:
        #     a, b = s[l].lower(), s[r].lower()
        #     if a.isalnum() and b.isalnum():
        #         if a != b: return False
        #         l += 1
        #         r -= 1
        #     l, r = l + (not a.isalnum()), r - (not b.isalnum())
        # return True
