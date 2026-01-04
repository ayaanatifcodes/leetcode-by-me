class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ''
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            new_str += word1[i]
            new_str += word2[i]

        if len(word1) > len(word2):
            new_str += word1[min_length:]
        else:
            new_str += word2[min_length:]
        return new_str