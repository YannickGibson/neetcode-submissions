class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
    # 0,1 - 0 + 1 = 1
    # 0,2 - 0 + 1 + 2 = 3
    # 0,3 - 0 + 1 + 2 + 3 = 6
    # 0,4 -               = 10
    # 0,5 -               = 15