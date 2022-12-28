string=input("enter any string:-")
substring=input("enter the substring you want to find in given string:-")
if string.find(substring)==-1:
    print("substring is not found")
else:
    print("substring is found")