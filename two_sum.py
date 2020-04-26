lst=[2,7,11,15]
t=9
sum=0
for i in lst:
    sum+=i
    if sum==t:
        print(lst.index(i))
        break