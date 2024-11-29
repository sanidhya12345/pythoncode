#print all the permutations of the list

from itertools import permutations

l=[1,2,3]

perm=permutations(l)
for i in perm:
    print(i)