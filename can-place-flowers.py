from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                left_side_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_side_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if left_side and right_side:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0

