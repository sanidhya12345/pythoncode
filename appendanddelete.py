s="hackerhappy"
t="hackerrank"
k=9
matched=0

m=min(len(s),len(t))

for i in range(m):
    if s[i]==t[i]:
        matched+=1
    elif s[i]!=t[i]:
        break
removed=len(s)-matched
append=len(t)-matched

if removed+append<=k:
    print(True)
else:
    print(False)