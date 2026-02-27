class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            string += word1[i]
            string += word2[i]
        if len(word1) > len(word2):
            string += word1[min_length:]
        else:
            string += word2[min_length:]
        return string

