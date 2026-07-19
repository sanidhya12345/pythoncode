class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)
        right = [0] * n
        left = [0] * n
        
        right[n - 1] = n - 1
        left[0] = 0
    
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                right[i] = right[i + 1]
            else:
                right[i] = i
                
        for i in range(1, n):
            if arr[i] <= arr[i - 1]:
                left[i] = left[i - 1]
            else:
                left[i] = i
                
        result = []
        for l, r in queries:
           
            if right[l] >= left[r]:
                result.append(True)
            else:
                result.append(False)
                
        return result