from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                x = board[r][c]
                if x == ".": continue
                if x in rows[r]: return False
                if x in cols[c]: return False
                if x in squares[(r // 3, c // 3)]: return False
                rows[r].add(x)
                cols[c].add(x)
                squares[(r // 3, c // 3)].add(x)
        return True