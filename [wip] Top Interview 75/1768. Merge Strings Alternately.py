class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for i in range(max(word1, word2)):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])

        return res
