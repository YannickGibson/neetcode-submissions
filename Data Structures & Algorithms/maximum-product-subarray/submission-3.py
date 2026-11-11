class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mi, ma = 1, 1  # each mi and ma remembers j till curr i of product
        for num in nums:
            tmp = mi
            mi = min(mi * num, ma * num, num)
            ma = max(tmp * num, ma * num, num)
            res = max(res, ma)
            
        return res