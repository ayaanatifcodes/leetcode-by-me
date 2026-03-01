from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        maxCandies = max(candies)
        for candy in candies:
            results.append(candy + extraCandies >= maxCandies)
        return results

# /**
#  * @param {number[]} candies
#  * @param {number} extraCandies
#  * @return {boolean[]}
#  */
# var kidsWithCandies = function(candies, extraCandies) {
#     let results = []
#     let max_Candies = Math.max(...candies)
#
#     for(let i = 0; i < candies.length; i++) {
#         results[i] = candies[i] + extraCandies >= max_Candies
#     }
#
#     return results
# };
