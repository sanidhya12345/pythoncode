l=input().split("x")
row=eval(l[0]) # i represents rows of cells
col=eval(l[1])# j represents columns of the cells
c=0
for i in range(0,row):
    for j in range(i,col):
        if (i+j)%2==0:
            c+=1
print(c)


def updateList(L):
    L[-1] = input("Enter the item which you want to update:")
    pass
def addList(L):
    L.append(input("enter the item which you want to add"))
    print(L)

lst = input().split(",")
updateList(lst)
addList(lst)
