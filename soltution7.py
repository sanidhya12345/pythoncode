n=int(input("Enter the number of students:-"))
l1=[]
l2=[]
l3=[]
for i in range(0,n):
    email=input("Enter email:-")
    l=email.split("@")
    l1.append(l[0])
    l2.append(l[1])
    l3.append(email)
names=tuple(l1)
domain=tuple(l2)
email=tuple(l3)
print(names)
print(domain)
print(email)

