from collections import deque

def bfs(adj,s):
    queue=deque()
    
    visited=[False]*len(adj)
    level=[0]*(len(adj))
    queue.append(s)
    visited[s]=True
    level[s]=0
    res=[]
    while queue:
        curr=queue.popleft()
        res.append(curr)
        
        for x in adj[curr]:
            if not visited[x]:
                queue.append(x)
                visited[x]=True
                level[x]=level[curr]+1
    print(level)
    return res            
adj = [[2,3,1], [0], [0,4], [0], [2]]
print(bfs(adj,0))