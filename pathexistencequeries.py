from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        def bs_helper(nums, key, n):
            low = 0
            high = n - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= key:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        # Setup DSU (Disjoint Set Union) arrays
        parent = list(range(n))
        
        # Finds the root group of a node
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        # Merges two nodes into the same group
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for i in range(0, len(nums)):
            u = i
            v = bs_helper(nums, nums[i] + maxDiff, n)
            
            # Connect the start node to the furthest reachable node
            union(u, v)
            
            #we must also link the immediate next node to ensure the 
            # whole chain between u and v stays connected in the same group.
            if i + 1 <= v:
                union(i, i + 1)
        result = [False] * len(queries)
        for k, (u, v) in enumerate(queries):
            # If they share the same parent, a path of ANY length exists!
            if find(u) == find(v):
                result[k] = True
            else:
                result[k] = False
                
        return result