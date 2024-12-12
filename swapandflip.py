# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    c=0
    for i in range(n):
        if s1[i]!=s2[i]:
            c+=1
    if c%2==0:
        print("YES")
    else:
        print("NO")
