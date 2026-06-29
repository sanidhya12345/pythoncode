#optimized approach using dp:

def countBinaryStrings(n,k):

    if k>=n:
        return 0
    
    MOD=10**9+7

    #dp[i][j][last_bit]
    '''
    i=string length
    j=count of adjacent '1's
    last_bit=0 or 1 

    if we are adding 0 then count of j remains same
    dp[i][j][0]=dp[i-1][j][0]+dp[i-1][j][1]

    if we are adding 1 then two cases will be there:
    case 1: last_bit=0 then no effect on j
    case 2: last_bit=1 then 
    dp[i][j][1]=dp[i-1][j][0]+dp[i-1][j-1][1]
    '''

    # Initalize the dp table

    dp=[[[0,0] for _ in range(k+1)] for _ in range(n+1)]
    dp[1][0][0]=1 # string "0" 0 adjacent 1s
    dp[1][0][1]=1 # string "1" 0 adjacent 1s

    for i in range(2,n+1):
        for j in range(k+1):

            # appending 0 in the last string
            dp[i][j][0]=(dp[i-1][j][0]+dp[i-1][j][1])%MOD

            # append 1 in the last string

            dp[i][j][1]=dp[i-1][j][0]%MOD

            if j>0:
                dp[i][j][1]=(dp[i][j][1]+dp[i-1][j-1][1])% MOD
            
    ans=(dp[n][k][0]+dp[n][k][1])%MOD

    return ans


#Bruteforce approach using sliding window
def slidingwindow(bit,n,k):
    i=0
    j=0
    c_adj=0
    while j<n:

        # size of current window is less than w
        if (j-i+1)<2:
            j+=1
        elif j-i+1==2:
            if bit[j]=='1' and bit[i]=='1':
                c_adj+=1
            i+=1    
            j+=1
    return c_adj==k

n=5
k=2
bits=["00","01","10","11"]
for i in range(n-2):
    bits=bits*2
    m=len(bits)
    for j in range(0,m//2):
        bits[j]="0"+bits[j]
    for l in range(m//2,m):
        bits[l]="1"+bits[l]
ans=0
for i in bits:
    if slidingwindow(i,len(i),k):
        ans+=1
print(ans)

print(countBinaryStrings(n,k))
