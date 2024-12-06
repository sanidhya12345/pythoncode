def palin(s,ans,index):
    #base case
    if index<0:
        return ans
    ans+=s[index]
    return palin(s,ans,index-1)
s=input()
ans=palin(s,"",len(s)-1)
if ans==s:
    print(True)
else:
    print(False)