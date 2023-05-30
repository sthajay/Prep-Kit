# 2114. Maximum Number of Words Found in Sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return sorted([(len(el.split(' '))) for el in sentences], reverse=True)[0]

        # Other Solution
        # return max(el.count(' ') for el in sentences) + 1
