class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  
            return False
        str = str(x)
        reversed_str = ""
        for i in range(len(s) - 1, -1, -1):
            reversed_str += s[i]
        return str == reversed_str
