class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels for fast O(1) lookup
        count = 0  # Stores number of vowels in current window
        for i in range(k):  # Count vowels in the first window of size k
            if s[i] in vowels:  # If current character is a vowel
                count += 1  # Increase vowel count
        max_vowels = count  # Initialize maximum with first window's count
        for i in range(k, len(s)):  # Slide the window through the string
            if s[i] in vowels:  # If new character entering window is vowel
                count += 1  # Add it to count
            if s[i - k] in vowels:  # If character leaving window is vowel
                count -= 1  # Remove it from count
            if count > max_vowels:  # Update maximum if current window is larger
                max_vowels = count
            if max_vowels == k:  # Early exit: can't have more than k vowels
                return k
        return max_vowels  # Return maximum vowels found in any window
