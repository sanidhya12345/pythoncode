l=[]
n=int(input("Enter the number of elements you want to insert:-"))
for i in range(0,n):
    s=int(input())
    l.append(s)
ele=int(input("Enter the element to search:-"))
for i in l:
    if i==ele:
        print("Element",i,"found at location",l.index(i)+1)
