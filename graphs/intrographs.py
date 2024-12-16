v=5
e=7
edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
graph=[[] for _ in range(v+1)]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
print(graph)