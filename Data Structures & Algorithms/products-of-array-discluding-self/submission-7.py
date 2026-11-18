from itertools import accumulate

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        right = [0] * len(nums)
        left = [0] * len(nums)
        r_roll = 1
        l_roll = 1
        for i in range(len(nums)):
            j = len(nums) - 1 - i 
            r_roll *= nums[i]
            l_roll *= nums[j]
            right[i] = r_roll
            left[j] = l_roll

        res = [0] * len(nums)
        for i in range(len(nums)):
            r = right[i - 1] if i - 1 >= 0 else 1
            l = left[i + 1] if i + 1 < len(nums) else 1
            res[i] = r * l
        return res