from collections import deque
def bfs(adj,visited,node,V):
    queue=deque()
    queue.append(node)
    visited[node]=True
    while queue:
        curr=queue.popleft()        
        for neighbour in range(V):
            if adj[curr][neighbour]==1 and not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour]=True

adj=[[1,0,1],[0,1,0],[1,0,1]]
V=3
visited=[False]*V
count=0
for i in range(V):
    if not visited[i]:
        bfs(adj,visited,i,V)
        count+=1
print(count)