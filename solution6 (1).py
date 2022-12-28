l=[]
n=int(input("Enter the number of element:-"))
for i in range(0,n):
    num=int(input())
    l.append(num)
dct={i:l.count(i) for i in l}
for i in dct:
    print(i,"found",dct.get(i),"times")