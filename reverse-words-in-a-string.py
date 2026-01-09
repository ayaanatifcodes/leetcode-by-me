class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.strip() 
        new_s = new_s.split()   
        length = len(new_s) 
        
        for i in range(length // 2):
            extra_s = new_s[i]
            new_s[i] = new_s[length - 1 - i]
            new_s[length - 1 - i] = extra_s

        return " ".join(new_s)