# 347. Top K Frequent Elements
# My Solution: https://leetcode.com/problems/top-k-frequent-elements/solutions/3573078/one-line-solution-beats-9318/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        for el in (Counter(nums).most_common()):
            k -= 1
            if k < 0:
                break
            m, v = el
            arr.append(m)
        return arr

    # One line solution
        # return list(dict(Counter(nums).most_common()).keys())[:k]
