from collections import defaultdict
def twosum(l,k):
    map=defaultdict()
    for i in l:
        if k-i in map:
            return True
        map[i]=True
    return False
l=list(map(int,input().split()))
k=int(input())
print(twosum(l,k))


