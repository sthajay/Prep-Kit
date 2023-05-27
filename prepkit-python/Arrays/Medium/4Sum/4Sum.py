# 18. 4Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                p3 = p2 + 1
                p4 = n - 1
                while p3 < p4:
                    sum = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    if sum > target:
                        p4 -= 1
                    elif sum < target:
                        p3 += 1
                    else:
                        ans.add((nums[p1], nums[p2], nums[p3], nums[p4]))
                        p4 -= 1
                        p3 += 1
        return ans
