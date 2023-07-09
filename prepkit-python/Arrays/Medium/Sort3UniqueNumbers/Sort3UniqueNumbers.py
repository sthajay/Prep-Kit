'''
Google Interview Question

Given a list of numbers with only 3 unique numbers(1, 2, 3),
sort the list in O(n) times.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

Try sorting the list using constant space.
'''


class Solution:
    def sort3UniqueNumbers(self, nums):
        count_1 = 0
        count_2 = 0
        count_3 = 0

        for el in nums:
            if el == 1:
                count_1 += 1
            elif el == 2:
                count_2 += 1
            elif el == 3:
                count_3 += 1

        index = 0
        for _ in range(count_1):
            nums[index] = 1
            index += 1

        for _ in range(count_2):
            nums[index] = 2
            index += 1

        for _ in range(count_3):
            nums[index] = 3
            index += 1

        return nums


sol = Solution()
sorted_nums = sol.sort3UniqueNumbers([3, 3, 2, 1, 3, 2, 1, 3, 3])
print(sorted_nums)
