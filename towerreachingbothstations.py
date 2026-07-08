from collections import deque

class Solution:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def countCoordinates(self, mat):
        
        def bfs(mat, n, m, q, reachable):
            while q:
                row, col = q.popleft()
                
                for k in range(4):
        
                    nr, nc = row + self.dx[k], col + self.dy[k]
                    
                    if (0 <= nr < n and 0 <= nc < m) and not reachable[nr][nc] and mat[nr][nc] >= mat[row][col]:
                        reachable[nr][nc] = True
                        q.append((nr, nc))
        
        n = len(mat)
        m = len(mat[0])
        
        stationP = deque()
        stationQ = deque()
        
        reachP = [[False]*m for _ in range(n)]
        reachQ = [[False]*m for _ in range(n)]
        
        for j in range(m):
            stationP.append((0, j))
            reachP[0][j] = True
            
            stationQ.append((n-1, j))
            reachQ[n-1][j] = True
            
        for i in range(n):
            stationP.append((i, 0))
            reachP[i][0] = True
    
            stationQ.append((i, m-1))
            reachQ[i][m-1] = True
        
        # FIX: Added the missing comma here
        bfs(mat, n, m, stationP, reachP)
        bfs(mat, n, m, stationQ, reachQ)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if reachP[i][j] and reachQ[i][j]:
                    count += 1

        return count