class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        mi, ma = 1, 1

        for num in nums:
            if num == 0:
                mi, ma = 1, 1
                continue
            tmp_mi = mi
            mi = min(mi * num, ma * num, num)
            ma = max(ma * num, tmp_mi * num, num)
            res = max(res, ma)

        return res