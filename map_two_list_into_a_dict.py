lst1=input().split(",")
lst2=input().split(",")
d={lst1[i]:lst2[i] for i in range(len(lst1))}
print(d)
