class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        res = -1

        while i < j:
            a, b = heights[i], heights[j]
            res = max(res, min(a, b) * (j - i))
            if a < b:
                i += 1  # i could not improve our area whatsoever
            elif a > b:
                j -= 1  # i will never improve result
            else:
                # hm -> doesn not matter, both are redundant
                i += 1
                j -= 1
        return res
            