class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # lets create adjacency list as 1 -> (2, 1) : A -> (B, W)

        edges = {i: [] for i in range(1, n+1)}
        for i in times:
            edges[i[0]].append((i[1], i[2]))
        
        heap = [(0,k)]
        # keep track of visited nodes
        visited = set()
        delays = 0
        # heap helps with getting the nearest node
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            # because we are tracking max time taken by signal to reach
            delays = max(time, delays)
            for nei in edges[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time+nei[1], nei[0]))

        return delays if len(visited) == n else -1