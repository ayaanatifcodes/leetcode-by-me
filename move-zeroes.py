from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_array = []
        zero_array = []
        for num in nums:
            if num != 0:
                num_array.append(num)
            else:
                zero_array.append(num)
        nums[:] = num_array + zeroes_array
