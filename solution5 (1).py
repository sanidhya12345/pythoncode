l=[]
res=[]
n=int(input("Enter the number of elements:-"))
for i in range(0,n):
    inp=input()
    l.append(inp)
for i in l:
    if i.isnumeric():
        s=i[::-1]
        res.append(int(s))
    else:
        res.append(i[::-1])
print(res)
