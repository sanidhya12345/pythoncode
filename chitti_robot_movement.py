def apna_fun(str,moves):
    if str in moves:
        print("false")
    else:
        print("true")

s=str(input())
m=["ll","rr","dd","uu","UU","LL","RR","DD"]
apna_fun(s,m)
