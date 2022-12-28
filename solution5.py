l=list(map(int,input().split(" ")))
n=int(input("Enter the search element:-"))
for i in l:
    if i==n:
        print("Number",n,"found at",l.index(i))
        break
    else:
        continue