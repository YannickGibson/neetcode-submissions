class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        rolling = 0
        for num in nums:
            if rolling < 0:
                rolling = 0
            rolling += num
            res = max(res, rolling)
        return res
            