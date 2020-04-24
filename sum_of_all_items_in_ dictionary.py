lst1=input().split(",")
lst2=input().split(",")
sum=0
d={lst1[i]:lst2[i] for i in range(len(lst1))}
for j in list(d.values()):
    sum+=eval(j)
print(sum)
