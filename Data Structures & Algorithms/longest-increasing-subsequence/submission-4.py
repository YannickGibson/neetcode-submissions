class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 9,1,4,2,3,1, 3,7]
        # |
        #   |
        #   | |
        #   |   |
        #   |   | |
        #   |   2 3
        #   1   2 3      7
        # 9,1,4,2,3,1, 3,7]
        # [4,5,6, 3,7]
        #

        dp = defaultdict(int)
        def dfs(max_val, index):

            if index >= len(nums):
                return 0
            

            # choose at index
            val1 = -1
            if nums[index] > max_val:
                if dp[index] > 0:
                    val1 = dp[index]
                else:
                    val1 = dfs(nums[index], index + 1) + 1
                    dp[index] = val1
 
            # skip to index + 1
            val2 = dfs(max_val, index + 1)
            return max(val1, val2)

        return dfs(max_val=float("-inf"), index=0)