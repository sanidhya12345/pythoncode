n=int(input("Enter the number of students:-"))
l=[]
for i in range(0,n):
    name=input()
    marks=int(input())
    l.append([name,marks])
dct={i+1:l[i] for i in range(len(l))}
for i in range(0,n):
    if dct.get(i+1)[1]>=75:
        print(dct.get(i+1)[0])
