n=int(input())
l=list(map(int,input().split(" ")))
s=sum(l)
totalsum= (n*(n+1))//2
print(totalsum-s)