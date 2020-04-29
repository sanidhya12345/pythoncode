lst=list(map(int,input().split(",")))
target=int(input())
lst.sort()
l=[]
for i in lst:
    if i==target:
        a=lst.index(i)
        print(a)
    if i!=target:
        lst.append(target)
        lst.sort()
        a=lst.index(target)
        print(a)
        break