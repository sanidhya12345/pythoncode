from typing import List


def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:

    
    def singleshift(arr,n):

        last=arr[n-1]
        arr[n-1]=0
        for i in range(n-1,0,-1):
            arr[i]=arr[i]+arr[i-1]
            arr[i-1]=0
        arr[0]=last

        return arr
    
    def shift(grid,m,n):

        for i in range(m):

            grid[i]=singleshift(grid[i],n)

        lastcol=grid[m-1][0]

        grid[m-1][0]=0

        for i in range(m-1,0,-1):
            grid[i][0]=grid[i][0]+grid[i-1][0]
            grid[i-1][0]=0
        grid[0][0]=lastcol

        return grid
        

    m=len(grid)
    n=len(grid[0])

    for i in range(k):
        grid=shift(grid,m,n)

    return grid


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(shiftGrid(grid,k))
