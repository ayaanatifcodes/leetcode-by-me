class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  
            return False
        string = str(x)
        reversed_string = ""
        for i in range(len(s) - 1, -1, -1):
            reversed_string += s[i]
        return string == reversed_string
