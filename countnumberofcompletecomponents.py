import collections
from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=collections.defaultdict(list)
        for i in range(n):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def bfs(s,visited):
            q=collections.deque([s])
            visited.add(s)
            nodes=0
            edges=0
            while q:
                u=q.popleft()
                nodes+=1
                for v in graph[u]:
                    edges+=1
                    if v!=[] and v not in visited:
                            q.append((v))
                            visited.add(v)
            return [nodes,edges//2]

        visited=set()
        comp=0
        for i in range(n):
            if i not in visited:
                nodes,edges=bfs(i,visited)
                if edges==(nodes*(nodes-1))//2:
                    comp+=1
        return comp