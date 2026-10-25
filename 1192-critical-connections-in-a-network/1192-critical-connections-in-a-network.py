class Solution:
    def criticalConnections(
        self,
        n: int,
        connections: list[list[int]]
    ) -> list[list[int]]:

        adj = [[] for _ in range(n)]

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        timer = 1
        tin = [-1] * n
        low = [-1] * n
        bridges = []

        def dfs(node, parent):
            nonlocal timer

            tin[node] = low[node] = timer
            timer += 1

            for nei in adj[node]:

                # Ignore the edge we came from
                if nei == parent:
                    continue

                # Neighbour is not visited
                if tin[nei] == -1:
                    dfs(nei, node)

                    # Update low-link value
                    low[node] = min(low[node], low[nei])

                    # Bridge condition
                    if low[nei] > tin[node]:
                        bridges.append([node, nei])

                else:
                    # Back edge
                    low[node] = min(low[node], tin[nei])

        dfs(0, -1)

        return bridges