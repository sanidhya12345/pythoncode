# how to define a function:

def add(a,b):
    return a+b
c=10
d=20
e=add(c,d)
print(e)

# Write a function to calculate area and perimeter of a rectangle.

def area(a,b):
    return a*b
def peri(c,d):
    return (c+d)*2
e=int(input())
f=int(input())
p=area(e,f)
q=peri(e,f)
print(p)
print(q)

# Write a function to calculate area and circumference of a circle.

def area(a):
    return a*a*3.14
def circumference(b):
    return b*2*3.14
c=int(input())
d=area(c)
e=circumference(c)
print("%0.2f"%d)
print("%0.2f"%e)


# Write a function to calculate power of a number raised to other.

def pow(a,b):
    return a**b
d=int(input())
e=int(input())
c=pow(d,e)
print(c)

# Write a function to tell user if he/she is able to vote or not.

def vote(a):
    if a>=18:
        print("he/she is able to vote.")
    else:
        print("he/she is not able to vote.")
age=int(input())
vote(age)

# Write a function to check if a number is even or not.

def even_or_not(a):
    if a%2==0:
        print("no.is even")
    else:
        print("no. is not even")
num=int(input())
even_or_not(num)


