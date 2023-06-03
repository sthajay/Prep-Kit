# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        n = len(unique_nums)
        if n == 0 or n == 1:
            return n
        nums = sorted(unique_nums)
        count = 0
        obj = dict()
        for i in range(n - 1):
            if nums[i] + 1 == nums[i+1]:
                if count in obj:
                    obj[count] += 1
                else:
                    obj[count] = 1
            else:
                count += 1
                obj[count] = 0
        return max(obj.values()) + 1
