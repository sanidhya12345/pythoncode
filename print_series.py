n=int(input("Enter the value of n:-"))
sum=0
for i in range(0,n):
    for j in range(0,i+1):
        sum+=(j+1)
print(sum)
