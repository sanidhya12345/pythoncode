#we will use recursion to solve the dfs traversal of the graph
ans=[]
def dfs(adj,visited,s):
    visited[s]=True
    ans.append(s)
    for i in adj[s]:
        if not visited[i]:
            dfs(adj,visited,i)

adj = [[2,3,1], [0], [0,4], [0], [2]]
visited=[False]*(len(adj))
dfs(adj,visited,0)
print(ans)