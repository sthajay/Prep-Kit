# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time Complexity = O(n) Linear
        # Space Complexity = O(1) Constant extra space
        l, r = 0, len(numbers) - 1
        while l < r:
            total_sum = numbers[l] + numbers[r]
            if total_sum == target:
                return [l + 1, r + 1]
            elif total_sum > target:
                r -= 1
            else:
                l += 1
        return []

        # Time and Memory Complexity = O(n)
        # obj = {}
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if numbers[i] in obj:
        #         return [obj[numbers[i]] + 1, i+1]
        #     else:
        #         obj[diff] = i
