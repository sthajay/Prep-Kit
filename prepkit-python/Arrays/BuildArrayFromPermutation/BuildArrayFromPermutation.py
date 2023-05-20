# 1920. Build Array from Permutation
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #   Defining length of variable, need to be of same length
        ans = [0]*len(nums)
        for el in range(0, len(nums)):
            ans[el] = nums[nums[el]]
        return ans

    # Optimal Single line solution
    # return [nums[i] for i in nums]
