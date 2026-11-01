class Solution:
    def canJump(self, nums: List[int]) -> bool:

        explored = {}
        n = len(nums)

        def jump(index):
            if index == n - 1: return True

            if index in explored:
                return False
            
            max_jump = min(nums[index], n - 1 - index)
            res = False
            for dist in range(1, max_jump + 1):
                res |= jump(index + dist)
            
            explored[index] = res
            return res

        return jump(index=0)


