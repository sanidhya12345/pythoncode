#create dp array outside the recursive function and use constraints value to take the dimension of the dp matrix

dp=[[-1 for _ in range(1002)] for _ in range(102)]
def knapMemo(weight,profit,W,n):
    
    #base condition 
    if n==0 or W==0:
        return 0
    
    if dp[n][W]!=-1:
        return dp[n][W]
    
    elif weight[n-1]<=W:
        dp[n][W]=max(profit[n-1]+knapMemo(weight,profit,W-weight[n-1],n-1),knapMemo(weight,profit,W,n-1))
        return dp[n][W]
    
    dp[n][W]=knapMemo(weight,profit,W,n-1)
    return dp[n][W]

n=3
W=3
profit=[1,2,3]
weight=[4,5,1]
print(knapMemo(weight,profit,W,n))