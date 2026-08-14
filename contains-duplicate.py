class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        added_vals = set()
        for n in nums:
            if n in added_vals:
                return True
            added_vals.add(n)
        return False
