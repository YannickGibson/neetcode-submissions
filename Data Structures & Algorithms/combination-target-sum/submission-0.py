class Solution:
    def combinationSum(self, nums: List[int], _target: int) -> List[List[int]]:
        res = set()
        nums.sort()

        # O(n^n)
        #nums=[2,5,6,9]
        #_target = 9
        # curr = set()
        # target = 9
        # -> curr = set([2])
        # -> target = 7
        #    -> curr = {2, 2}
        #    -> target = 5
        #    -> curr = {2, 5}
        #    -> target = 2
        #    -> curr = {2, 6}
        #    -> target = 2
        #    -> curr = {2, 9}
        # -> curr = set([5])
        # -> target = 4
        # -> curr = set([6])
        # -> target = 3
        # -> curr = set([9])
        # -> target = 0 -> add frozen set
        def dfs(curr, target, index):
            if target < 0:
                return
            if target == 0:
                res.add(curr)
                return
            
            for i in range(index, len(nums)):
                dfs(curr + (nums[i],), target - nums[i], i)
            
            


        dfs(tuple(), _target, 0)


        return [list(x) for x in res if res]