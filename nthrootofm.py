def nthRoot(n,m):
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        pro=1
        for _ in range(0,n):
            pro*=mid
        if pro==m:
            return mid
        elif pro<m:
            low=mid+1
        else:
            high=mid-1
    return -1

n,m=map(int,input().split())
print(nthRoot(n,m))