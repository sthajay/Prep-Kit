# 1481. Least Number of Unique Integers after K Removals
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        sortVal = sorted(counter.values())
        ans = len(sortVal)
        for i in sortVal:
            k -= i
            if k < 0:
                break
            ans -= 1
        return ans

    # Other Solution
        # c = Counter(arr)
        # s = sorted(arr,key = lambda x:(c[x],x))
        # return len(set(s[k:]))
