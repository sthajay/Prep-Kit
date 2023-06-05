# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        p1, p2 = 0, len(height) - 1
        while p1 < p2:
            if height[p1] > height[p2]:
                max_area = max(max_area, height[p2] * (p2 - p1))
                p2 -= 1
            else:
                max_area = max(max_area, height[p1] * (p2 - p1))
                p1 += 1
        return max_area

        # Brute force solution , Time complexity = O(n^2)
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(1, len(height)):
        #         total = min(height[i], height[j]) * abs(i-j)
        #         if total > max_area:
        #             max_area = total
        # return max_area
