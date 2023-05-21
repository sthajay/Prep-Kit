# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxVal = max(candies)
        for el in candies:
            if (el + extraCandies) >= maxVal:
                ans.append(True)
            else:
                ans.append(False)
        return ans

    # Other Solution
        # maxVal = max(candies)
        # return [el + extraCandies >= maxVal  for el in candies]
