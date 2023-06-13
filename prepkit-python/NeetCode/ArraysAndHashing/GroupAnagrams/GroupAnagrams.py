# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimized Solution : time complexity = O(m * n)
        obj = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            obj[tuple(count)].append(s)
        return obj.values()

        # Other solution
        # obj = dict()  : Time complexity  = O(m * nlogn)
        # for el in strs:
        #     sorted_word = ''.join(sorted(el))
        #     if sorted_word in obj:
        #         obj[sorted_word].append(el)
        #     else:
        #         obj[sorted_word] = [el]
        # return [i for i in obj.values()]
