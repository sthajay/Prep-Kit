# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = 10000000
        closest_sum = 0
        n = len(nums)
        nums.sort()
        for p1 in range(n - 2):
            p2 = p1 + 1
            p3 = n - 1
            while p2 < p3:
                sum = nums[p1] + nums[p2] + nums[p3]
                if sum > target:
                    p3 -= 1
                elif sum < target:
                    p2 += 1
                else:
                    return sum
                diff = abs(sum - target)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = sum
        return closest_sum
