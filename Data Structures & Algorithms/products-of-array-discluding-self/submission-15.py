from itertools import accumulate

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        r_roll = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = r_roll
            r_roll *= nums[j]

        l_roll = 1
        for i in range(len(nums)):
            res[i] = res[i] * l_roll
            l_roll *= nums[i]
        return res