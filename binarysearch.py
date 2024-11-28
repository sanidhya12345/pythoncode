def binaryHelper(l,target):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==target:
            return True
        elif l[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return False
n,q=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
l.sort()
for _ in range(q):
    e=int(input())
    if binaryHelper(l,e):
        print("found")
    else:
        print("not found")
        