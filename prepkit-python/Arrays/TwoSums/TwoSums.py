# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            val = target - nums[i]
            if val in nums:
                if (i != nums.index(val)):
                    ans.append(nums.index(val))
                    ans.append(i)
                    break
        return ans

    # Optimal solution
        # dict = {}
        # for i, n in enumerate(nums):
        #     if n in dict:
        #         return [dict[n], i]
        #     dict[target-n] = i
