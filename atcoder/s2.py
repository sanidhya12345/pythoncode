n, d = map(int, input().split())
s = list(input()) 

for i in range(n - 1, -1, -1):
    if s[i] == '@' and d > 0:
        s[i] = '.' 
        d -= 1      
print("".join(s))