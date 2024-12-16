from collections import deque
def bfs(row,col,visited,grid,n,m):
    queue=deque()
    queue.append((row,col))
    visited[row][col]=True
    
    while queue:
        curr=queue.popleft()
        r=curr[0]
        c=curr[1]
        
        #traverse in the neighbour and mark them if it is the land
        
        for delrow in range(-1,2):
            for delcol in range(-1,2):
                nrow=r+delrow;
                ncol=c+delcol
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]=='1' and not visited[nrow][ncol]:
                    visited[nrow][ncol]=True
                    queue.append((nrow,ncol))
                    
                
                

grid=[['1','1','0','0','0'],
        ['0','1','0','0','1'],
        ['1','0','0','1','1'],
        ['0','0','0','0','0'],
        ['1','0','1','1','0']]

n=len(grid)
m=len(grid[0])

visited=[[False for i in range(m)] for i in range(n)]
count=0
for row in range(n):
    for col in range(m):
        if not visited[row][col] and grid[row][col]=='1':
            count+=1
            bfs(row,col,visited,grid,n,m)
        
print(count)