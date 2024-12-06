def sm(n,s):
    if n==0:
        return s
    s+=n
    return sm(n-1,s)

n=int(input())
print(sm(n,0))