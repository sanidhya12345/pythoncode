s=[1,2,3]
n=len(s)
ans=[]
for mask in range(1<<n):
    l=[]
    for i in range(n):
        if mask & (1<<i):
            l.append(s[i])
    ans.append(l)
print(ans)