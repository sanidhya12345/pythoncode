from collections import deque

def maximumSafenessFactor(grid:list[list[int]])-> int:
    n=len(grid)

    # base case: if start or end has a theif, the path safeness is instantly 0/

    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return 0
    
    # Step1: multisource bfs to find distances to nearest theif

    dist=[[-1]*n for _ in range(n)]

    queue=deque()

    # add all the theives to the queue

    for r in range(n):
        for c in range(n):
            if grid[r][c]==1:
                queue.append((r,c))
                dist[r][c]=0
    
    directions=[(0,1),(0,-1),(1,0),(-1,0)]

    # run the bfs to populate the dist matrix

    while queue:

        r,c=queue.popleft()
        for dr,dc in directions:
            nr,nc=r+dr,c+dc

            if 0<=nr<n and 0<=nc<n and dist[nr][nc]==-1:
                dist[nr][nc]=dist[r][c]+1
                queue.append((nr,nc))
    

    # now we will check whether the path is possible or not

    def is_path_possible(safeness_limit):

        # if the start or end does not meet the limit reject it

        if dist[0][0]<safeness_limit or dist[n-1][n-1]<safeness_limit:
            return False
        
        queue=deque([(0,0)])
        visited=[[False]*n for _ in range(n)]

        visited[0][0]=True

        while queue:
            r,c=queue.popleft()

            # reached the destination

            if r==n-1 and c==n-1:
                return True
            
            for dr,dc in directions:
                nr,nc=r+dr,c+dc

                #Only visit the neighbors that meet the safeness threshold

                if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and dist[nr][nc]>=safeness_limit:
                    visited[nr][nc]=True
                    queue.append((nr,nc))
        return False
    
    # binary search on the answer so minimum safeness limit is 0 and maximum safeness limit is the minimum distance at the start or at the end point.

    low=0
    high=min(dist[0][0],dist[n-1][n-1])
    ans=0
    while low<=high:
        mid=(low+high)//2

        if is_path_possible(mid):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans