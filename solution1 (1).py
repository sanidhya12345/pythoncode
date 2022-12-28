l=[]
n=int(input("Enter the number of elements you want to insert:-"))
for i in range(0,n):
    s=int(input())
    l.append(s)
min=l[0]
max=l[0]
for i in l:
    if min>i:
        min=i
    if max<i:
        max=i
print("Max Val=",max)
print("Min Val=",min)