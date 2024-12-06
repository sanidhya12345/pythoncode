def floorSqrt(n): 
    low=1
    high=n//2
    while low<=high:
        mid=(low+high)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            low=mid+1
        else:
            high=mid-1
    return high
            
n=int(input())
print(floorSqrt(n))