import heapq

class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7
        
        pq = [-x for x in arr]
        heapq.heapify(pq) 
        
        maxamount = 0
        
        while k > 0 and pq:
           
            price = -heapq.heappop(pq)
            
            
            if price == 0:
                break
                
            maxamount = (maxamount + price) % MOD
            
            if price - 1 > 0:
                heapq.heappush(pq, -(price - 1))
                
            k -= 1
            
        return maxamount