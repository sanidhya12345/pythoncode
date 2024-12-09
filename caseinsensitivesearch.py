txt="aBcAb".lower()
pat="aB".lower()
n=len(txt)
#try with sliding window
k=len(pat)
i,j=0,0
l=[]
l1=[]
while j<n:
    if j-i+1<k:
        j+=1
    elif j-i+1==k:
        if txt[i:j+1]==pat:
            l.append(i)
        i+=1
        j+=1
print(l)