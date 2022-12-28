s=input("Enter the string:-")
res=""
for i in range(0,len(s)):
    if i%2!=0:
        res+=s[i]
    else:
        res+=s[i].upper()
print(res)