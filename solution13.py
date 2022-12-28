l=list(map(int,input().split(" ")))
ans=[]
for i in l:
    if i%2==0:
        ans.append(i/10)
    else:
        ans.append(i*2)
print(ans)