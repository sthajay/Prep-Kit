# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        obj = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if numbers[i] in obj:
                return [obj[numbers[i]] + 1, i+1]
            else:
                obj[diff] = i
