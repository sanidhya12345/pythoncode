n=int(input())
m=n
x=n%10
n=n//10
y=n%10
n=n//10
p=x**3
q=y**3
r=n**3
s=p+q+r
if s==m:
    print("armstrong")
else:
    print("not")
