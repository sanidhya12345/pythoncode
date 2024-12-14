s = "bxq   czlz ov twkxe"
l=s.split(" ")
lst=[]
for i in l:
    if i!='':
        lst.append(i)
ans=lst[0]
if len(lst)>1:
    if len(lst)>=1:
        for i in range(1,len(lst)):        
            char=chr(ord(lst[i][0])-32)
            rest=lst[i][1:]
            f=char+rest
            ans+=f
    
print(ans)