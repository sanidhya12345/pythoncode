n=int(input("Enter the number of students:-"))
l=[]
for i in range(0,n):
    mark1=int(input("Enter the marks of first subject:-"))
    mark2 = int(input("Enter the marks of second subject:-"))
    mark3 = int(input("Enter the marks of third subject:-"))
    l.append((mark1,mark2,mark3))
print(tuple(l))