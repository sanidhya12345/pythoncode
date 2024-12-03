def product(l):
    prefix=[1 for i in range(len(l))]
    suffix=[1 for i in range(len(l))]
    
    for i in range(1,len(l)):
        prefix[i]=prefix[i-1]*l[i-1]
    for i in range(len(l)-2,-1,-1):
        suffix[i]=suffix[i+1]*l[i+1]
    ans=[prefix[i]*suffix[i] for i in range(len(l))]
    return ans
l=list(map(int,input().split()))
print(product(l))