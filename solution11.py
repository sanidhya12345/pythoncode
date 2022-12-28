l1=list(input().split(" "))
l2=list(map(int,input().split(" ")))
dct={l1[i]:l2[i] for i in range(0,len(l1))}
sum_of_all_values=0
for i in dct:
    sum_of_all_values+=dct.get(i)
print(sum_of_all_values)