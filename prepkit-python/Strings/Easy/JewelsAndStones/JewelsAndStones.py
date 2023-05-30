# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for el in stones:
            if el in jewels:
                ans += 1
        return ans

    # Other Solution
        # ans = 0
        # for el in stones:
        #     ans += jewels.count(el)
        # return ans

        # return sum(jewels.count(el) for el in stones)
