# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        p, n, z = [], [], []

        for el in nums:
            if el == 0:
                z.append(el)
            elif el > 0:
                p.append(el)
            else:
                n.append(el)

        P, N = set(p), set(n)

        if z:
            if len(z) >= 3:
                ans.add((0, 0, 0))
            for el in N:
                if (-1 * el) in P:
                    ans.add((el, 0, -el))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    ans.add(tuple(sorted([target, n[i], n[j]])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    ans.add(tuple(sorted([target, p[i], p[j]])))

        return ans
