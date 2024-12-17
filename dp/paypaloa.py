s=input()
k=int(input())
dp=[0 for i in range(len(s)+1)]
dp[0]=1
maxLen=0
for i in range(1,len(s)):
    if abs(ord(s[i-1])-ord(s[i]))<=k:
        dp[i]=dp[i-1]+1
    else:
        dp[i]=1
print(max(dp))