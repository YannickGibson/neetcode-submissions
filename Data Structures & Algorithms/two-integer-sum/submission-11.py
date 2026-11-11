class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = [(nums[i], i) for i in range(len(nums))]
        vals.sort(key=lambda t: t[0])
        i, j = 0, len(nums) - 1

        while i < j:
            if vals[i][0] + vals[j][0] > target:
                # smaller num
                j -= 1
            elif vals[i][0] + vals[j][0] < target:
                i += 1
            else:
                a, b = vals[i][1], vals[j][1]
                if a<b:return [a,b]
                else: return [b,a]

        raise ValueError("Such pair does not exist")