l=list(map(int,input().split(" ")))
t=tuple(l)
max=t[0]
for i in l:
    if i%2!=0 and max<i:
        max=i
print(max)
