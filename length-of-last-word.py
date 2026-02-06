class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        word_length = 0
        for i in range (len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            word_length += 1
        return word_length
