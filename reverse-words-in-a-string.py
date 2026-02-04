from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.strip()
        new_s = new_s.split()
        s_length = len(new_s)
        for num in range(s_length // 2):
            extra_s = new_s[num]
            new_s[num] = new_s[s_length - 1 - num]
            new_s[s_length - 1 - num] = extra_s
        return" ".join(new_s)
