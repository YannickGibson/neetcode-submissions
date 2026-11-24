class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Bruteforce O(n^3)
        # -2, 0, 0, 1, 1, 1, 2, 2, 2
        nums.sort()
        def twoSum(index, target):
            i, j = index + 1, len(nums) - 1
            res = []  # -1, 0, 1, 2
            #            x     i  k
            while i < j:
                a, b = nums[i], nums[j]
                if target == a + b:
                    res.append([nums[i], nums[j]])
                    while i < len(nums) and nums[i] == a: i += 1
                    while j >= 0 and nums[j] == b: j -= 1
                else:
                    if target > a + b:
                        i += 1
                    else:
                        j -= 1
            return res

        res = []
        i = 0
        while i < len(nums) - 2:
            curr = nums[i]
            res.extend([[curr] + l for l in twoSum(i, target=-curr)])
            while i < len(nums) - 2 and nums[i] == curr:
                i += 1
        return res
                