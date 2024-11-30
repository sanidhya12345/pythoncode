n,q=map(int,input().split(" "))
l=list(map(int,input().split(" ")))

while q>0:
    left,right,val=map(int,input().split(" "))
    for i in range(left,right+1):
        l[i-1]+=val    
    q-=1    
print(*l)