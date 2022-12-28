t=("hello","world","hi","xyz")
res=t[len(min(t,key=len))]
print(res)