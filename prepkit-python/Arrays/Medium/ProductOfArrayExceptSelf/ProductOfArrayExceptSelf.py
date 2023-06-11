# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        left = 1
        right = 1
        for i in range(n):
            ans[i] *= left
            left *= nums[i]
            ans[n-i-1] *= right
            right *= nums[n-i-1]
        return ans

        # n = len(nums)
        # left = [0]*n
        # right = [0]*n
        # left[0] = 1
        # right[n-1] = 1
        # for i in range(1, n):
        #     left[i] = left[i-1] * nums[i-1]
        #     right[n-1-i] = right[n-i] * nums[n-i]
        # ans = []
        # for i in range(n):
        #     ans.append(left[i] * right[i])
        # return ans

    # Other Solution
        # length=len(nums)
        # sol=[1]*length
        # pre = 1
        # post = 1
        # for i in range(length):
        #     sol[i] *= pre
        #     pre = pre*nums[i]
        #     sol[length-i-1] *= post
        #     post = post*nums[length-i-1]
        # return(sol)
