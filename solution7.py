l=[]
n=int(input("Enter the number of elements:-"))
for i in range(0,n):
    inp=input()
    l.append(inp)
string=[]
numbers=[]
for i in l:
    if i.isnumeric():
        numbers.append(int(i))
    else:
        string.append(i)
print(string)
print(numbers)