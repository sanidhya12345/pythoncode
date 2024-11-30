n,d=map(int,input().split(" "))
s=input()
count_empty=0
count_cookie=0;

for i in s:
    if i=='.':
        count_empty+=1
for i in s:
    if i=='@':
        count_cookie+=1
        if count_cookie==d:
            break
print(count_cookie+count_empty)
