n,t=map(int,input().split(" "))
w=list(map(int,input().split(" ")))
for _ in range(t):
    s,e=map(int,input().split(" "))
    print(min(w[s:e+1]))
