def fact(n,ans):
    if n==1:
        return ans
    ans*=n
    return fact(n-1,ans)

n=int(input())
print(fact(n,1))
