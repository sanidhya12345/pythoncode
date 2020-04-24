l=list(map(int,input().split()))
count = [0 for x in range(10)]
p=[]
for i in l:
    p.append(str(i))
    num="".join(p)
string = str(num)
for i in range(len(string)):
        count[int(string[i])]=count[int(string[i])] + 1
r= 0
m= 1
for i in range(10):
        while count[i] > 0:
            r=r+(i*m)
            count[i]=count[i]-1
            m=m*10
print(r)


