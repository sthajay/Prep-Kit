# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        The overall time complexity is O(nlogn + n^2), which simplifies to O(n^2) 
        since the n^2 term dominates the nlogn term.

        The space complexity of this code is O(1) since it uses a constant amount of 
        additional space. The variables ans, initial_diff, l, r, threeSum, 
        and diff are the only variables used, and they occupy a constant
        amount of space regardless of the size of the input.
        '''
        nums.sort()
        ans = 0
        initial_diff = float('inf')
        for i, el in enumerate(nums):
            if i > 0 and el == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = el + nums[l] + nums[r]
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return threeSum
                diff = abs(target - threeSum)
                if diff < initial_diff:
                    initial_diff = diff
                    ans = threeSum
        return ans

        # Other Solution
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
