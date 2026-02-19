class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            new_string += word1[i]
            new_string += word2[i]
        if len(word1) > len(word2):
            new_string += word1[min_length:]
        else:
            new_string += word2[min_length:]
        return new_string
