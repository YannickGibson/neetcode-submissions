class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n + 1)
        
        if n == 1: return 1
        arr[-1] = 1
        arr[-2] = 1

        for i in reversed(range(len(arr) - 2)):
            arr[i] = arr[i+1] + arr[i+2]

        return arr[0]