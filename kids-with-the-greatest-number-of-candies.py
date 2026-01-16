from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        maxCandies = max(candies)
        for candy in candies:
            results.append(candy + extraCandies >= maxCandies)
        return results 
