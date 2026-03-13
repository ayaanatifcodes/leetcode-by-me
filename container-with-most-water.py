class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        results = 0
        while i < j:
            result = max(results, (j - i) * min(height[i], height[j]))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return result
