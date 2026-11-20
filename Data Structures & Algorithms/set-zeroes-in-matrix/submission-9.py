class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        SPECIAL = float("-inf")
        
        def dfs(i, j, direction, nullify, dry_run):  # return True if we nullify
            if i >= ROWS or j >= COLS: return nullify
            new_i = i + (1 if direction == "col" else 0)
            new_j = j + (1 if direction == "row" else 0)
            val = matrix[i][j]
            nullify |= val == 0  # propagate and update nullify information
            nullify |= dfs(new_i, new_j, direction, nullify, dry_run)
            if nullify and val != 0 and dry_run:  # receive information from parents
                matrix[i][j] = SPECIAL
            elif val == SPECIAL and not dry_run: 
                matrix[i][j] = 0
            elif nullify and val != 0 and not dry_run: 
                matrix[i][j] = 0
            #print(nullify, val)

            return nullify



        # 1. Row-wise: Set SPECIAL for vals to be changed to 0
        for r in range(ROWS):
            dfs(r, 0, direction="row", nullify=False, dry_run=True)
        #print(matrix)
        # 2. Col-wise: Set to 0 
        # 3. Set SPECIAL's to zero
        for c in range(COLS):
            dfs(0, c, direction="col", nullify=False, dry_run=False)
        return