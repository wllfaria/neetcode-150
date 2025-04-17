class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len({x for x in nums}) != len(nums)
