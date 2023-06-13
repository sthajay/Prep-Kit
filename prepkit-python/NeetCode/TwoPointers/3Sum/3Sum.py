# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 Pointers Solution - Same for 3Sum Closest
        nums.sort()
        n = len(nums)
        print(nums)
        arr = list()
        for p1 in range(n - 2):
            if p1 == 0 or nums[p1] != nums[p1 - 1]:
                p2 = p1 + 1
                p3 = n - 1
                while p2 < p3:
                    sum = nums[p1] + nums[p2] + nums[p3]
                    if sum == 0:
                        arr.append([nums[p1], nums[p2], nums[p3]])
                        while p2 < p3 and nums[p2] == nums[p2 + 1]:
                            p2 += 1
                        while p2 < p3 and nums[p3] == nums[p3 - 1]:
                            p3 -= 1
                        p2 += 1
                        p3 -= 1
                    elif sum > 0:
                        p3 -= 1
                    else:
                        p2 += 1

        return arr
        '''
        nums.sort()
        ans = set()
        p, n, z = [], [], []
        for el in nums:
            if el > 0:
                p.append(el)
            elif el < 0:
                n.append(el)
            else:
                z.append(el)

        P, N = set(p), set(n)

        if z:
            if len(z) >= 3:
                ans.add((0, 0, 0))
            for el in P:
                if -el in N:
                    ans.add((-el, 0, el))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    ans.add((p[i], p[j], target))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    ans.add((n[i], n[j], target))

        return ans
        # return [list(i) for i in ans]
        '''
