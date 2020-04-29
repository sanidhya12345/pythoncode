lst1=list(map(int,input().split(",")))
lst2=list(map(int,input().split(",")))
lst1.sort()
lst2.sort()
if 0 in lst1:
    for i in lst1:
        lst1.remove(0)
if 0 in lst2:
    for i in lst2:
        lst2.remove(0)
lst1.extend(lst2)
lst1.sort()
print(lst1)