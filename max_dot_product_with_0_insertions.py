class Solution:
    def maxDotProduct(self, a, b):
        m = len(b)
        n = len(a)
        
        # Invalid states ko -infinity se mark karo
        dp = [-float('inf')] * (m + 1)
        
        # Base case: 0 elements from b means dot product is 0
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(min(i, m), 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + (a[i - 1] * b[j - 1]))
                
        return dp[m]