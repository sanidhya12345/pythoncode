from collections import deque,defaultdict

from typing import List
def minScore(n: int, roads: List[List[int]]) -> int:


    graph=defaultdict(list)

    for u,v, dist in roads:
        graph[u].append((v,dist))
        graph[v].append((u,dist))
    

    minscore=float('inf')

    queue=deque([1])
    visited=set()
    visited.add(1)
    while queue:

        node=queue.popleft()
        
        for neighbor,dist in graph[node]:

            if minscore>dist:
                minscore=dist
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return minscore


n = 6
roads = [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]
print(minScore(n,roads))