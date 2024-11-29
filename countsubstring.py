def check(l):
    return all(l[i]<=l[i+1] for i in range(len(l)-1))

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split(" ")))
    c=0
    for i in range(0,n):
        for j in range(i,n):
            if check(l[i:j+1]):
                c+=1
    print(c)
