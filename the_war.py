l=input().split("x")
row=eval(l[0]) # i represents rows of cells
col=eval(l[1])# j represents columns of the cells
c=0
for i in range(0,row):
    for j in range(i,col):
        if (i+j)%2==0:
            c+=1
print(c)
