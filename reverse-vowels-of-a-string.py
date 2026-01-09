        vowels = set("aeiouAEIOU") # A set of vowels
        s = list(s) # s is converted to a list       
        left, right = 0, len(s) - 1 # Left is '0' and right is length - 1 as first element is index 0

        while left < right: # Left less than right
            if s[left] not in vowels: # if the character is a vowel
                left += 1 # Increment left
            elif s[right] not in vowels: # Right letter not in vowels
                right -= 1 # Decrement right
            else: 
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
