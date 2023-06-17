# 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # In other language, the value (l+r) might overflow but not in py
            # To fix in other language, we have to do this:
            m = l + ((r-l) // 2)
            # m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
