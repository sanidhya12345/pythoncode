class Solution:
    def maxPathSum(self, a, b):
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        
        sum1 = 0  # To track sum of current segment in array 'a'
        sum2 = 0  # To track sum of current segment in array 'b'
        finalans = 0
        
        while i < n and j < m:
            if a[i] < b[j]:
                sum1 += a[i]
                i += 1
            elif a[i] > b[j]:
                sum2 += b[j]
                j += 1
            else:
                # Common element found! 
                # Take max of the path sums up to this point + the common element
                finalans += max(sum1, sum2) + a[i]
                
                # Reset sums for the next segment
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
                
        while i < n:
            sum1 += a[i]
            i += 1
            
        while j < m:
            sum2 += b[j]
            j += 1
            
        # Add the maximum of the remaining parts of both arrays
        finalans += max(sum1, sum2)
        
        return finalans