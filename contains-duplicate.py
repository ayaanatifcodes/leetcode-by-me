class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        added_values = set()
        for n in nums:
            if n in added_values:
                return True
            added_values.add(n)
        return False
