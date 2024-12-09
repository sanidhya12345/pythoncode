from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    p=input()
    #hashmap will store the character with their exchanged character.
    map=defaultdict()
    for i in range(0,26):
        map[p[i]]=p[25-i]
        map[p[25-i]]=p[i]
    
    dp=[[float('inf')]*2 for _ in range(n)]
    dp[0][0]=0
    dp[0][1]=1
    for i in range(1,n):
        #if i-1 and i are already in sorted order no change.
        if s[i-1]<=s[i]:
            dp[i][0]=dp[i-1][0]
        #there is only option to change i-1
        if map[s[i-1]]<=s[i]:
            dp[i][0]=min(dp[i][0],dp[i-1][1])
        if s[i-1]<=map[s[i]]:
            dp[i][1]=1+dp[i-1][0]
        if map[s[i-1]]<=map[s[i]]:
            dp[i][1]=min(dp[i][1],1+dp[i-1][1])
    ans=min(dp[n-1][0],dp[n-1][1])
    if ans!=float('inf'):
        print(ans)
    else:
        print(-1)
        
    