
'''
number=int(input())
s=str(number)
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

'''

'''
number=int(input())
snum=number
rev=0
while snum!=0:
    m=snum%10
    rev=rev*10+m
    snum=snum//10
if rev==number:
    print("palindrome")
else:
    print("not palindrome")
'''
'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
    '''
'''
C=float(input("enter any temperature"))
F=C*9/5+32
print(F)
'''
'''
miles=int(input("Enter distance into miles:-"))
km=miles/0.621371
print("distance in km",km)
'''
'''''''''''
a=int(input("Enter any number1:-"))
b=int(input("Enter any number2:-"))
c=int(input("Enter any number3:-"))
print("original numbers",a,b,c)
a,b,c=a,a+b,b+c+a
print("after swaping the numbers",a,b,c)
'''''
'''
x=int(input("enter value of x:"))
y=int(input("enter value of y :"))
z=int(input("enter value of z: "))
print("Individually workers A,B,C takes x,y,z days to complete the work",x,y,z)
days=(x*y*z)/(x*y+y*z+x*z)
print("the number of days if they work(A,B,C) together",days)
'''
x=int(input("enter value of x:"))
y=int(input("enter value of y :"))
z=int(input("enter value of z: "))
print("numbers before swapping",x,y,z)
x,y=y,x
z,x=x,z
print("after swapping",x,y,z)



