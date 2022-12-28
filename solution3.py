l=list(map(int,input().split(" ")))
min=l[0]
min_index=0
for i in range(0,len(l)):
    if min>l[i]:
        min=l[i]
        min_index=i
print("Minimum Element:-",min)
print("Index of minimum element:-",min_index)