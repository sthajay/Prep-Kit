# 1528. Shuffle String
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        obj = dict()
        ans = ''
        for i in range(len(indices)):
            obj[indices[i]] = s[i]
        for el in sorted(obj.items()):
            k, v = el
            ans = ans + v
        return ans

    # Other solution
        # ans = [''] * len(s)
        # for i in range(len(s)):
        #     ans[indices[i]] = s[i]
        # return ('').join(ans)
