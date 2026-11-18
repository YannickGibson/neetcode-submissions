from itertools import accumulate

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        r_roll = 1
        for j in range(len(nums) - 1, -1, -1):
            r_roll *= nums[j]
            res[j] = r_roll

        l_roll = 1
        for i in range(len(nums)):
            r = res[i + 1] if i + 1 < len(nums) else 1
            res[i] = r * l_roll
            l_roll *= nums[i]
        return res