lst1=list(map(int,input().split(",")))
lst2=list(map(int,input().split(",")))
lst1.sort()
lst2.sort()
if lst1==[] and lst2==[]:
    print("median is 0")
else:
    c=0
    lst1.extend(lst2)
    for i in lst1:
        c+=1
    if c%2==0:
        median=((c//2)+((c//2)+1))/2
        print(median)
    else:
        median=(c+1)/2
        print(median)