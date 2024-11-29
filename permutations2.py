from itertools import permutations

nums=[1,1,2]

s=set()
perm=permutations(nums)

for i in perm:
    s.add(i)

l=[]
for i in s:
    l.append(list(i))
print(l)