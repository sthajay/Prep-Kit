# 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gp = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j and nums[i] == nums[j]):
                    gp += 1
        return gp

        # Other Solution
        # gp = 0
        # dist = {}
        # for el in nums:
        #     if el in dist:
        #         if dist[el] == 1:
        #             gp += 1
        #         else: gp += dist[el]
        #         dist[el] += 1
        #     else:
        #         dist[el] = 1
        #         print(el, dist)
        # return gp
