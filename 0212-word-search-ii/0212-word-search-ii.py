class Solution:
    def findWords(self, board, words):
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = w
        m, n = len(board), len(board[0])
        ans = []
        def dfs(i, j, node):
            if i < 0 or i >= m or j < 0 or j >= n: return
            c = board[i][j]
            if c not in node: return
            node = node[c]
            if '#' in node:
                ans.append(node.pop('#'))
            board[i][j] = '.'
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(i + di, j + dj, node)
            board[i][j] = c
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return ans