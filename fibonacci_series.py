n=int(input("Enter the number of terms you want to print:- "))
a=0
b=1
count=0
if n<=0:
    print("Please enter the valid number of terms.")
elif n==1:
    print("Fibonacci series upto",n,":-",a)
else:
    print("Fibonacci sequence is:-")
    while count<n:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
        count+=1
