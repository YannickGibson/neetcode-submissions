class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            # What needs to happen for us not to be watered by this tile
            if r < 0 or c < 0 or c >= COLS or r >= ROWS or (r, c) in visited or prev_height > heights[r][c]:
                return
            visited.add((r, c))
            v = heights[r][c]
            dfs(r + 1, c, visited, v)
            dfs(r - 1, c, visited, v)
            dfs(r, c + 1, visited, v)
            dfs(r, c - 1, visited, v)


        # Fload starting from rows
        for c in range(COLS):
            dfs(0, c, pac, float("-inf"))
            dfs(ROWS - 1, c, atl, float("-inf"))

        # Fload starting from cols
        for r in range(ROWS):
            dfs(r, 0, pac, float("-inf"))
            dfs(r, COLS - 1, atl, float("-inf"))

        # Check what positions are in both sets
        res = []
        for c in range(COLS):
            for r in range(ROWS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res