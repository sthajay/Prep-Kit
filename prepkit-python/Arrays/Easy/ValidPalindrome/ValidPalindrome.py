# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern ='[^0-9a-zA-Z]+'
        clean_string = re.sub(pattern, '', s.lower())
        print(clean_string)
        return clean_string == clean_string[::-1]
    
    # Other Solution
        # 1
        # s = [el for el in s.lower() if el.isalnum()]
        # return s == s[::-1]

        # 2. Two pointer Solution
        
        # p1, p2 = 0, len(s) - 1
        # while p1 < p2:
        #     a, b = s[p1].lower(), s[p2].lower()
        #     if a.isalnum() and b.isalnum():
        #         if a != b: return False
        #         p1 += 1
        #         p2 -= 1
        #     p1, p2 = p1 + (not a.isalnum()), p2 - (not b.isalnum())
        # return True
