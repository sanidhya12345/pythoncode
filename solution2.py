val=[]
n=int(input("Enter the number of elements you want to insert:-"))
for i in range(0,n):
    s=int(input())
    val.append(s)
if n%2!=0:
    n=n-1
for i in range(0,n,2):
    val[i],val[i+1]=val[i+1],val[i]
print(val)