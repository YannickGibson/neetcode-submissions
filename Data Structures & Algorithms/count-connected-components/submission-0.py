class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Union-Find
        parent = list(range(n))
        rank = [1] * n
        n_components = n
        for edge in edges:
            a, b = edge
            a_root, b_root = a, b
            while parent[a_root] != a_root: a_root = parent[a_root]
            while parent[b_root] != b_root: b_root = parent[b_root]
            if a_root != b_root:
                n_components -= 1
                if rank[a_root] < rank[b_root]:
                    parent[b_root] = a_root
                else:
                    if rank[a_root] == rank[b_root]:
                        rank[a_root] += 1
                    parent[a_root] = b_root
            
        return n_components
                