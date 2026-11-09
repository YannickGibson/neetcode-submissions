class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 0, 0, 3, 4, 3
        # r1,r2,

        def house_robber1(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(nums[0], house_robber1(nums[1:]), house_robber1(nums[:-1]))