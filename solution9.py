l=list(map(int,input().split(" ")))
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Odd list:-",odd)
print("Even list:-",even)
