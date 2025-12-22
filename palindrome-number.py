class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  
            return False
       
        s = str(x)
        reversed_s = ""


        for i in range(len(s) - 1, -1, -1):
            reversed_s += s[i]
        return s == reversed_s