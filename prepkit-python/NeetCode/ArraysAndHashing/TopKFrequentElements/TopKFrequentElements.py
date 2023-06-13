# 347. Top K Frequent Elements
# My Solution: https://leetcode.com/problems/top-k-frequent-elements/solutions/3573078/one-line-solution-beats-9318/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Linear solution.  Time complexity = O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for el in nums:
            if el in count:
                count[el] += 1
            else:
                count[el] = 1

        for key, val in count.items():
            freq[val].append(key)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                result.append(v)
                if len(result) == k:
                    return result

    # One line solution
        # return list(dict(Counter(nums).most_common()).keys())[:k]
