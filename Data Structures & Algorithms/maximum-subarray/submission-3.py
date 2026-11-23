class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        left_sums = [0] * len(nums)
        left = [0] * len(nums)
        left_min = 0
        right_sums = [0] * len(nums)
        right = [0] * len(nums)
        right_min = 0
        full_sum = sum(nums)
        rolling = 0
        for i in reversed(range(len(nums))):
            rolling += nums[i]
            right_sums[i] = rolling
            if right_sums[i] < right_min:
                right_min = right_sums[i]
            right[i] = right_min

        rolling = 0
        for i in range(len(nums)):
            rolling += nums[i]
            left_sums[i] = rolling
            if left_sums[i] < left_min:
                left_min = left_sums[i]
            left[i] = left_min

        res = max(full_sum - left[-2], full_sum - right[1])
        for i in range(1, len(nums) - 1):
            res = max(res, full_sum - left[i - 1] - right[i + 1])

        return res
