class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Preparate Union-Find
        n_islands = 0
        parents = {}
        ranks = {}
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                parents[(i, j)] = (i, j)
                ranks[(i, j)] = 1
                if val == "1": n_islands += 1
        
        def find(a):
            # find parent
            if parents[a] == a: return a
            return find(parents[a])
        
        def union(a, b):
            # union two parents
            if ranks[a] > ranks[b]:
                # put b under a
                parents[b] = a
            else:
                parents[a] = b
                if ranks[a] == ranks[b]:
                    ranks[b] += 1
        
        # Start merging parents
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if grid[i][j] == "0": continue
                for di, dj in ((0, 1), (1, 0)):
                    ni, nj = i + di, j + dj
                    if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]):
                        if grid[ni][nj] == "1":
                            # merge the two cells (i.e their parents)
                            a, b = find((i, j)), find((ni, nj))
                            if a != b:
                                n_islands -= 1
                                union(a, b)
        return n_islands

