class Solution:
    def rob(self, nums: List[int]) -> int:


        if len(nums) <= 2:
            return max(nums)

        best = nums.copy()
        best[-3] += best[-1]

        for i in range(len(best) - 1 - 3, -1, -1):
            best[i] += max(best[i + 2], best[i + 3])

        return max(best[0], best[1])