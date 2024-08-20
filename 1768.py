class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        len1, len2 = len(word1), len(word2)

        for i in range(min(len1, len2)):
            res += word1[i]
            res += word2[i]

        if len1 > len2:
            res += word1[len2:]
        elif len2 < len1:
            res += word2[len1:]
        
        return res

