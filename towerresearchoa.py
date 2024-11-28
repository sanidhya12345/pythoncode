from math import gcd
from collections import defaultdict,deque
from functools import reduce

def lcm(a,b):
    return (a*b)//gcd(a,b)

def component_size(l,p):
    n=len(l) 
    graph={l[i]:p[i] for i in range(n)} #directed graph
    visited={node:False for node in l} #visited map
    csize=[] #component size
    def bfs(start):#bfs used to find the connected components with their sizes
        queue = deque([start])
        size = 0
        while queue:
            node = queue.popleft()
            size += 1
            visited[node] = True
            next_node = graph[node]
            if not visited[next_node]:
                queue.append(next_node)
        return size
    
    for node in l:
        if not visited[node]:
            size=bfs(node)
            csize.append(size) #append component size in the list
    return csize

def final_ans(l,p):
    comp_size=component_size(l,p)
    return reduce(lcm,comp_size)

n=int(input())
p=list(map(int,input().split(" ")))
l=[i for i in range(1,n+1)]
print(final_ans(l,p))

    