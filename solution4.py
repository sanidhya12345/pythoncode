l=input().split(" ")
smallest_string=l[0]
min_index=0
for i in range(0,len(l)):
    if len(smallest_string)>len(l[i]):
        smallest_string=l[i]
        min_index=i
print("Smallest String:-",smallest_string)
print("Smallest String Index:-",min_index)