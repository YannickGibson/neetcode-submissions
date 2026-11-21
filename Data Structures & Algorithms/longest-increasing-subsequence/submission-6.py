class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP O(n^2)


        lis = [1] * len(nums)

        for l in reversed(range(len(nums) - 1)):
            best_len = 1  # If we choose nothing
            for r in range(l + 1, len(nums)):
                if nums[l] < nums[r] and best_len < lis[r] + 1:
                    best_len = lis[r] + 1
            lis[l] = best_len
        return max(lis)