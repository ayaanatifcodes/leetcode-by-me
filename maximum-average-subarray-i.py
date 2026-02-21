class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        window_sum = sum(nums[left:right]) # nums[start:end] so for this 3 elements are covered
        max_sum = window_sum
        while right < len(nums):
            window_sum = window_sum - nums[left] + nums[right] # Using sliding window to update current value
            max_sum = max(max_sum, window_sum)
            left += 1
            right += 1
        return max_sum / k

