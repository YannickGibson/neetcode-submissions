class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}  # diff: index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[num] = i
        raise ValueError("Invalid input: no possible combination matching target.")