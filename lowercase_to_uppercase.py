def case_conver(str):
    for i in str:
        if ord(i)>=65 and ord(i)<=90:
            a=chr(ord(i)+32)
            if ord(i)==72:
                a=chr(ord(i))
        if ord(i)>=97 and ord(i)<=122:
            a=chr(ord(i)-32)
            if ord(i)==104:
                a=chr(ord(i))
        print("".join(a),end="")
s=input()
case_conver(s)
