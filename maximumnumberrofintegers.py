
def max_count(banned,n,maxsum):
    l=[]
    for i in range(1,n+1):
       if i not in banned:
           l.append(i)
    sm=0
    count=0
    for i in l:
        sm+=i
        if sm<=maxsum:
            count+=1
    return count 
banned=[11]
n=7
maxsum=50

print(max_count(banned,n,maxsum))