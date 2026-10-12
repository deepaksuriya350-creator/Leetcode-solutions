class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [False] * n
        depth = [0] * n

        def has_odd_cycle(node, parent, curr):
            vis[node] = True
            depth[node] = curr

            for nbr in graph[node]:
                if nbr == parent:
                    continue
                if not vis[nbr]:
                    if has_odd_cycle(nbr, node, curr + 1):
                        return True
                else:
                    cycle_length = abs(depth[node] - depth[nbr]) + 1
                    if cycle_length % 2 == 1:
                        return True
            return False

        for i in range(n):
            if not vis[i] and has_odd_cycle(i, -1, 0):
                return False
        return True