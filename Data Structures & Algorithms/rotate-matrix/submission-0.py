class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        

        l, r = 0, len(matrix) - 1
        # Make l, r come closer 
        while l < r:
            t, b = l, r
            for i in range(0, r - l):
                tmp = matrix[t][l + i]  # top row
                matrix[t][l + i] = matrix[b - i][l]  # top row <- left col
                matrix[b - i][l] = matrix[b][r - i]  # left col <- bottom row
                matrix[b][r - i] = matrix[t + i][r]  # bottom row <- right col
                matrix[t + i][r] = tmp # right col <- top row
            l += 1
            r -= 1

