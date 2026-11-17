class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        variable_seen = set()
        for i in nums:
            if i in variable_seen:
                return True
            variable_seen.add(i)
        return False
           