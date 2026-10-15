import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        heap=[(grid[0][0],0,0)]
        ans=0
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        visited=[[0 for i in range(n)] for j in range(n)]
        while heap:
            val, i, j= heapq.heappop(heap)
            if i==n-1 and j==n-1:
                return max(ans,val)
            if visited[i][j]:
                continue
            ans=max(ans,val)
            
            visited[i][j]=1
            for i1,j1 in dirs:
                i2=i+i1
                j2=j+j1
                if 0<=i2<n and 0<=j2<n and visited[i2][j2]==0:
                    heapq.heappush(heap, (grid[i2][j2], i2, j2))