from itertools import accumulate

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        right = list(accumulate(nums, lambda a, b: a * b))
        left = list(reversed(list(accumulate(reversed(nums), lambda a, b: a * b))))

        res = []
        for i in range(len(nums)):
            r = right[i - 1] if i - 1 >= 0 else 1
            l = left[i + 1] if i + 1 < len(nums) else 1
            res.append(r * l)
        return res