t=int(input())
for _ in range(t):
    n=int(input())
    ans=[]
    l=list(map(int,input().split(" ")))
    for i in range(0,n):
        for j in range(i,n):
            b=max(l[i:j+1])
            ans.append(b)
    print(*ans)