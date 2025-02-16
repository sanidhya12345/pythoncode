n=int(input())
m=n
reverse=0

while m!=0:
    digit=m%10
    reverse=reverse*10+digit
    m=m//10
if reverse==n:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")