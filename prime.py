n=int(input())
if n>1:
    for i in range(2,n):
        if n%2==0:
            print("number is not prime")
            break

    else:
            print("number is prime")
