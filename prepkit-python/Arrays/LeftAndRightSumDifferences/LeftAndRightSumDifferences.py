# 2574. Left and Right Sum Differences
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        leftsum = [0]*len(nums)
        rightsum = [0]*len(nums)
        total = sum(nums)
        ans = [0]*len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                rightsum[i] = total - n
            elif i == (len(nums) - 1):
                leftsum[i] = total - rightsum[i-1]
            else:
                leftsum[i] = total - rightsum[i-1]
                rightsum[i] = total - n - leftsum[i]
            ans[i] = abs(leftsum[i] - rightsum[i])
        return ans

    # Other solution
        # return [abs(sum(nums[:i + 1]) - sum(nums[i:])) for i in range(len(nums))]
