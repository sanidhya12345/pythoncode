d={'apple': 1, 'mango': 2, 'orange': 3, 'apple': 4}
l=list(d.keys())
z=0
for i in l:
    l.count(i)
    if z>1:
        d.remove(i)
print(d)