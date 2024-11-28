Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
n=int(input())
s=input()
if n==1:
    ans=""
    for i in s:
        f=Original.find(i)
        ans+=Key[f]
    print(ans)
else:
    ans=""
    for i in s:
        f=Key.find(i)
        ans+=Original[f]
    print(ans)