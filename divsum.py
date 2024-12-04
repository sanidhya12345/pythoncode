def calsum(n):
    l=[i for i in range(1,n) if n%i==0]
    return sum(l)
    
t=int(input())
for _ in range(t):
    n=int(input())
    print(calsum(n))