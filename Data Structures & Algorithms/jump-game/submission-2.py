class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        can_reach = [False] * n  # [False, False, False, False, False]
        can_reach[-1] = True  # [False, False, False, False, True]
        
        for i in range(n - 2, -1, -1): # n-2, n-3, ..., 2, 1, 0
            for j in range(1, nums[i] + 1):
                jump_to = i + j
                if jump_to < n and can_reach[jump_to] == True:
                    can_reach[i] = True
        return can_reach[0]


        explored = {}

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


