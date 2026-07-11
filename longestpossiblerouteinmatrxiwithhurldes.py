class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
       
        if not mat or len(mat) == 0 or len(mat[0]) == 0:
            return -1
        
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        n = len(mat)
        m = len(mat[0])
        
        self.max_length = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x, y, current_len):
            if x == xd and y == yd:
                self.max_length = max(self.max_length, current_len)
                return
            
            mat[x][y] = 0
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                    dfs(nx, ny, current_len + 1)
                    
            mat[x][y] = 1
        
        dfs(xs, ys, 0)
        
        return self.max_length