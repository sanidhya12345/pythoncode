s=str(input("Enter any string:- "))
count=0
for i in s:
    if i.islower()==True:
        count=count+1
print(count)