class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            reduced = [x for x in row if x != "."]
            if len(reduced) != len(set(reduced)):
                return False
        
        # Check columns
        for x in range(9):
            row = set()
            for y in range(9):
                val = board[y][x]
                if val != ".":
                    if val in row:
                        return False
                    row.add(val)
        
        # Check subgrids
        for j in range(3):
            for i in range(3):
                bag = set()
                # Get every field in the subgrid
                for y in range(j * 3, (j + 1) * 3):
                    for x in range(i * 3, (i + 1) * 3):
                        val = board[y][x]
                        if val != ".":
                            if val in bag:
                                return False
                            bag.add(val)
        return True