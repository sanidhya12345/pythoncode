s="vanshika"
#how to find the length of a given string..
print(len(s))

#find the character of a given string at position 4.
print(s[4])

#how to find the index of a character in a string..

print(s.index('h'))# .index method is used to find the index of a character of a string..

#iteration of a orstring..

#method1:-
for i in range(0,len(s)):
    print(s[i],end="")
print()

#method2:-
for i in s:
    print(i,end="")
print()
#slicing:-

print(s[0:2])

#how to reverse a string...

print(s[::-1])

#convert the given string into uppercase..

print(s.upper()[::-1])
tuple
#convert the string s="VANSHIKA" into lowercase..

print(s.lower())

#concatenation of string..

s1="vanshika"
s2="laddo"
print(s1+s2)

#print a string number of times...

s3="helloo "
print(s3*3)
print(s3[0]*2)

#capitalize the string.

a="good"
print(a.capitalize())

b="vanshika is a good girl"
print(b.title())

#uppercase every other character of a string...
c="vanshika"
res=""
for i in range(0,len(c)):
    if i%2==0:
        res=res+c[i].upper()
    else:
        res=res+c[i]
print(res)

#check whether the given string is in uppercase or not..

d="vanshika"
e="VANSHIKA"
print(d.isupper())#false
print(e.isupper())#true
print(d.islower())#true
print(e.islower())#false

#join method:-

f="vanshika"

print("*".join(f))

#program that asks the user for a string and creates the string that doubles each character of original string.

#input:- help
#output:- hheellpp

inp="help"
out=""
for i in range(0,len(inp)):
    out=out+inp[i]*2
print(out)

#write a program to input a string and check if contains a digit or not..

s="eueskjsjqaudhiug"
for i in s:
    if i>='0' and i<='9':
        print("yes found")
        break
else:
        print("not found")


















































