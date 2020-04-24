print("hello world")

#2. two-fer

s=input()
print("one for %s"%s,"one for me")

#3.raindrops:-

num=int(input())
if num%3==0:
    print("pling",end="")
if num%5==0:
    print("plang",end="")
if num%7==0:
    print("plong",end="")
if num%3!=0 and num%5!=0 and num%7!=0:
    print(num)

