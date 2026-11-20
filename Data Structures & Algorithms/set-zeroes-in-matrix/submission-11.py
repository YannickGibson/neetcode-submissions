class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        

        # use first row except first val to mark cols to be zeroesd
        # use first col for rows to be removed

        zero_first_col = False
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if c == 0:
                        zero_first_col = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0

        # zero values except first row and col
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(COLS):
                matrix[0][c] = 0
        if zero_first_col:
            for r in range(ROWS):
                matrix[r][0] = 0

        return


        