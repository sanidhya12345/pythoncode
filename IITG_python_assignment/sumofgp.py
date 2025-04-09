start=int(input())
n=int(input())
sum=start

for i in range(0,n):
    sum=sum+(start**2)//2
    start=sum
print(sum)
