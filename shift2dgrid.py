# from typing import List


# def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:

    
#     def singleshift(arr,n):

#         last=arr[n-1]
#         arr[n-1]=0
#         for i in range(n-1,0,-1):
#             arr[i]=arr[i]+arr[i-1]
#             arr[i-1]=0
#         arr[0]=last

#         return arr
    
#     def shift(grid,m,n):

#         for i in range(m):

#             grid[i]=singleshift(grid[i],n)

#         lastcol=grid[m-1][0]

#         grid[m-1][0]=0

#         for i in range(m-1,0,-1):
#             grid[i][0]=grid[i][0]+grid[i-1][0]
#             grid[i-1][0]=0
#         grid[0][0]=lastcol

#         return grid
        

#     m=len(grid)
#     n=len(grid[0])

#     for i in range(k):
#         grid=shift(grid,m,n)

#     return grid


# grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
# k = 4
# print(shiftGrid(grid,k))


# Optimized code  
from typing import List

def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    n_cols = len(grid[0])
    
    # 1. Flatten the 2D grid into a 1D list using a list comprehension
    flat_grid = [num for row in grid for num in row]
    
    # 2. Modulo k by the total number of elements to avoid redundant shifts
    k %= len(flat_grid)
    
    # 3. Shift the array in one fell swoop using Python slicing
    if k > 0:
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        
    # 4. Reconstruct and return the 2D grid
    return [flat_grid[i : i + n_cols] for i in range(0, len(flat_grid), n_cols)]


# --- Test Case ---
grid = [[3,8,1,9], [19,7,2,5], [4,6,11,10], [12,0,21,13]]
k = 4
print(shiftGrid(grid, k))