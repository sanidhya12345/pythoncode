s = "tab a cat"
string="".join([i for i in s if i.isalnum()])
string=string.lower()
i=0
j=len(string)-1

while i<=j:
    if string[i]==string[j]:
        i+=1
        j-=1
    if string[i]!=string[j]:
        break
if i>j:
    print(True)
else:
    print(False)
    