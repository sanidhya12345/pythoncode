def solve(n,x,a,b):
    coins=sorted(zip(a,b),reverse=True,key=lambda x: x[0])
    total_value = sum(a * b for a, b in coins)
    if total_value<x:
        return -1
    remaining=x
    distinct_types=0
    for value, count in coins:
        max_contribution = value * count
        if remaining > 0:
            distinct_types += 1
            if max_contribution >= remaining:
                remaining = 0
                break
            else:
                remaining -= max_contribution
    if remaining>0:
        return -1
    return distinct_types

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(solve(n,x,a,b))
    