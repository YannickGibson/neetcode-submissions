class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)