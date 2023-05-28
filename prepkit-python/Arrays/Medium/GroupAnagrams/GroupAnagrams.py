# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = dict()
        for el in strs:
            sorted_word = ''.join(sorted(el))
            if sorted_word in obj:
                obj[sorted_word].append(el)
            else:
                obj[sorted_word] = [el]
        return [i for i in obj.values()]
